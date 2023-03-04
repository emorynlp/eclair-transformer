from typing import List, Dict, Tuple, Union

import datasets
import torch
from datasets import DatasetDict
from transformers import Trainer, TrainingArguments, BertTokenizer, DataCollatorWithPadding, RobertaTokenizer, BertForSequenceClassification, RobertaForSequenceClassification

T1 = 'T1'
T2 = 'T2'
T1_LABEL_LIST = ['NQ', 'CRCI', 'CRCII', 'CRCIII', 'CRCIV']
T2_LABEL_LIST = ['NO', 'YES']
T1_LABEL_DICT = {label: idx for idx, label in enumerate(T1_LABEL_LIST)}
T2_LABEL_DICT = {label: idx for idx, label in enumerate(T2_LABEL_LIST)}


class ECLAIRTransformer:
    def __init__(self, task: str = None, encoder: str = None, model_path: str = None, device: int = 0):
        """
        If the model path is specified, it initializes by loading the trained model.
        Otherwise, it initializes for the specified task using the specific encoder.
        :param task: T1 (Task 1) or T2 (Task 2).
        :param encoder: 'bert-*' (e.g., 'bert-large-cased') or 'roberta-*' (e.g., 'roberta-large').
        :param model_path: the path to a trained model.
        :param device: 0 (default) or a positive integer n to use the nth GPU; a negative integer to use CPU.
        """
        self.device = torch.device('cuda:{}'.format(device) if device >= 0 and torch.cuda.is_available() else 'cpu')

        if model_path is None:
            if task is None or encoder is None:
                raise Exception('Either (task & encoder) or (model_path) must be specified.')

            num_labels = len(T1_LABEL_LIST) if task == T1 else len(T2_LABEL_LIST)

            if encoder.startswith('bert'):
                self.model = BertForSequenceClassification.from_pretrained(encoder, num_labels=num_labels).to(self.device)
            elif encoder.startswith('roberta'):
                self.model = RobertaForSequenceClassification.from_pretrained(encoder, num_labels=num_labels).to(self.device)
            else:
                raise Exception('Only Bert- or RoBERTa-based encoders are supported.')
        else:
            self.model = torch.load(model_path).to(self.device)
            encoder = self.model.config.architectures[0]

        self.tokenizer = BertTokenizer.from_pretrained(encoder) if encoder.startswith('bert') else RobertaTokenizer.from_pretrained(encoder)

    def save(self, model_path: str):
        """
        :param model_path: the path to the model file to be saved.
        """
        torch.save(self.model, model_path)

    def train(self, trn_data: List[Dict], dev_data: List[Dict], lr: float = 2e-5, epochs: int = 3, output_dir: str = '.'):
        """
        :param trn_data: the training data; a list of dictionaries where each dictionary represents a resume.
        :param dev_data: the development data; a list of dictionaries where each dictionary represents a resume.
        :param lr: the learning rate.
        :param epochs: the number of epochs.
        :param output_dir: the output directory to write the model predictions and checkpoints.
        """
        dataset = self.dataset_dict(trn_data, dev_data)
        data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        data = dataset.map(lambda x: self.tokenizer(x['text'], truncation=True), batched=True)

        training_args = TrainingArguments(
            output_dir=output_dir,
            learning_rate=lr,
            per_device_train_batch_size=2,
            per_device_eval_batch_size=2,
            gradient_accumulation_steps=8,
            num_train_epochs=epochs,
            weight_decay=0.01,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=data['train'],
            eval_dataset=data['eval'],
            tokenizer=self.tokenizer,
            data_collator=data_collator,
        )

        trainer.train()

    def decode(self, resume: Dict[str, str]) -> Dict[str, Union[float, Tuple[str, float]]]:
        """
        :param resume: a dictionary representing a resume.
        :return: a dictionary comprising all labels as keys and their scores as values. It also contains the key 'best', whose value is [best_label, best_score].
        """
        ext = self.extract(resume)
        tokenized_data = self.tokenizer(ext, truncation=True, return_tensors='pt')['input_ids'].to(self.device)
        output = self.model(tokenized_data).logits
        p = torch.nn.functional.softmax(output, dim=1)[0]
        ref = self.label_list()
        rt = [(ref[idx], elem.item()) for idx, elem in enumerate(p)]
        res = dict(rt)
        res['best'] = max(rt, key=lambda x: x[1])
        return res

    def dataset_dict(self, trn_data: List[Dict[str, str]], dev_data: List[Dict[str, str]]) -> DatasetDict:
        """
        :param trn_data: the training set; a list of dictionaries where each dictionary represents a resume.
        :param dev_data: the development set; a list of dictionaries where each dictionary represents a resume.
        :return: the dataset dictionary.
        """

        def create(data: List[Dict[str, str]]) -> List[Tuple[str, int]]:
            return [(self.extract(resume), ref[resume['Label']]) for resume in data]

        ref = self.label_dict()
        trn_text, trn_label = zip(*create(trn_data))
        dev_text, dev_label = zip(*create(dev_data))

        trn = datasets.Dataset.from_dict({'text': trn_text, 'label': trn_label})
        dev = datasets.Dataset.from_dict({'text': dev_text, 'label': dev_label})
        return datasets.DatasetDict({'train': trn, 'eval': dev})

    def extract(self, resume: Dict[str, str]) -> str:
        """
        :param resume: a dictionary representing a resume.
        The following keys are required for all tasks: 'Qualification', 'Certification', 'Experience', 'JobProfile'.
        The following key is required for T2: 'JobDescription'
        :return: a string that concatenates values from all required fields.
        """

        def preprocess(s: str) -> str:
            s = s.replace('\r', ' ')
            s = s.replace('\t', ' ')
            return ' '.join(s.split())

        res = [preprocess(resume[key]) for key in ['Qualification', 'Certification', 'Experience', 'JobProfile']]
        if self.task() == T2: res.append(preprocess(resume['JobDescription']))
        return ' '.join(res)

    def task(self) -> str:
        """
        :return: T1 if the model is for Task 1; otherwise, T2.
        """
        return T1 if self.model.config.num_labels == len(T1_LABEL_LIST) else T2

    def label_list(self) -> List[str]:
        """
        :return: T1_LABEL_DICT if the model is for Task 1; otherwise, T2_LABEL_DICT.
        """
        return T1_LABEL_LIST if self.task() == T1 else T2_LABEL_LIST

    def label_dict(self) -> Dict[str, int]:
        """
        :return: T1_LABEL_DICT if the model is for Task 1; otherwise, T2_LABEL_DICT.
        """
        return T1_LABEL_DICT if self.task() == T1 else T2_LABEL_DICT
