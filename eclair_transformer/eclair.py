import torch
import datasets

from transformers import Trainer, TrainingArguments, BertTokenizer, DataCollatorWithPadding, RobertaTokenizer, BertForSequenceClassification, RobertaForSequenceClassification

class ECLAIR:
    def __init__(self, model_name=None, task=1, type='bert'):
        if type == 'bert':
            self.type = 1
        else:
            self.type = 0
        self.set_task(task)
        self.model = self.load(model_name)
        self.set_tokenizer()

    def set_tokenizer(self):
        if self.type == 1:
            self.tokenizer = BertTokenizer.from_pretrained("bert-large-cased")
        elif self.type == 0:
            self.tokenizer = RobertaTokenizer.from_pretrained("roberta-large")

    def set_task(self, t):
        self.task = t
  
    def set_type(self, ty):
        if ty == 'bert':
            self.type = 1
        else:
            self.type = 0

    def load(self, model_name=None):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        if model_name != None:
            model = torch.load(model_name)         
            model = model.to(device)
            return model
        else:
            if self.type == 0:
                if self.task == 1:
                    return RobertaForSequenceClassification.from_pretrained("roberta-large", num_labels=5).to(device)
                else:
                    return RobertaForSequenceClassification.from_pretrained("roberta-large").to(device)
            elif self.type == 1:
                if self.task == 1:
                    return BertForSequenceClassification.from_pretrained("bert-large-cased", num_labels=5).to(device)
                else:
                    return BertForSequenceClassification.from_pretrained("bert-large-cased").to(device)
 
    def save(self, directory='/'):
        torch.save(self.model, directory)

    def train(self, dataset, lr=2e-5, epochs=3):
        model = self.model
        tokenizer = self.tokenizer
        dataset = self.dataset_prep(dataset)
        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
        def preprocess_function(examples):
            return tokenizer(examples["text"], truncation=True)

        data = dataset.map(preprocess_function, batched=True)

        training_args = TrainingArguments(
            output_dir="/local/scratch/bzhao44/ECLAIR/res/output",
            learning_rate=lr,
            per_device_train_batch_size=2,
            per_device_eval_batch_size=2,
            gradient_accumulation_steps=8,
            num_train_epochs=epochs,
            weight_decay=0.01,
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=data["train"],
            eval_dataset=data["eval"],
            tokenizer=tokenizer,
            data_collator=data_collator,
        )

        trainer.train()
    
    def dataset_prep(self, ls):
        if self.task == 1:
            ref = {'NQ': 0, 'CRCI': 1, 'CRCII': 2, 'CRCIII': 3, 'CRCIV': 4}
        else:
            ref = {'NO': 0, 'YES': 1}
        tset = ls["train"]
        eset = ls["eval"]
        tlb = []
        ttx = []
        elb = []
        etx = []
        for elem in tset:
            res = ECLAIR.extract(self, f=elem)
            ttx.append(res[0])
            tlb.append(ref[res[1]])
        for elem in eset:
            res = ECLAIR.extract(self, f=elem)
            etx.append(res[0])
            elb.append(ref[res[1]])
        
        trn = datasets.Dataset.from_dict({'text': ttx, 'label': tlb})
        eval = datasets.Dataset.from_dict({'text': etx, 'label': elb})
        dd = datasets.DatasetDict({"train": trn, "eval": eval})
        return dd
         
    def extract(self, f, lb=True):
        q = f['Qualification']
        c = f['Certification']
        e = f['Experience']
        jp = f['JobProfile']

        res = q + c + e + jp
        if not self.task == 1:
            jd = f['JobDescription']
            res += jd
        res = res.replace("\r", "")
        res = res.replace("\t", "")
        if not lb:
            return res
        else:
            l = f['Label']
            r = [res, l]
            return r
    
    def decode(self, s): # takes in a json object as input
        res = ECLAIR.extract(self, f=s, lb=False)
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        tokenized_data = self.tokenizer(res, truncation=True, return_tensors='pt')['input_ids'].to(device)
        model = self.model
        output = model(tokenized_data).logits
        p = torch.nn.functional.softmax(output, dim=1)[0]
        rt = []
        if self.task == 1:
            rev_ref = {0: "NQ", 1: "CRCI", 2: "CRCII", 3: "CRCIII", 4: "CRCIV"}
        else:
            rev_ref = {0: "NO", 1: "YES"}
        max = -1
        maxidx = -1
        for elem in p:
            rt.append(elem.item())
        for idx, elem in enumerate(rt):
            if elem > max:
                max = elem
                maxidx = idx
        if self.task == 1:
            parsed_res = [{"best_prediction": [[rev_ref[maxidx], max]], "predictions": {"NQ": rt[0], "CRCI": rt[1], "CRCII": rt[2], "CRCIII": rt[3], "CRCIV": rt[4]}}]
        else:
            parsed_res = [{"best_prediction": [[rev_ref[maxidx], max]], "predictions": {"NO": rt[0], "YES": rt[1]}}]
        return parsed_res
