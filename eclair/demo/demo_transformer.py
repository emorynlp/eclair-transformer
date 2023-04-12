import glob
import json
import os

from eclair.transformer import ECLAIRTransformer, T1, T2


def read_data(dir_path: str, splits_file: str, task: str):
    """
    :param dir_path: the path of the directory containing resume files in JSON.
    :param splits_file: the path to the file containing the labels (and job descriptions for T2).
    :return:
    """
    splits = json.load(open(splits_file))
    file_list = []
    for synset in splits:
        file_name = str(synset["resume_id"]) + ".json"
        file_path = os.path.join(dir_path, file_name)
        file_content = json.load(open(file_path))
        if task == T1:
            file_content["t1_label"] = synset["t1_label"]
        elif task == T2:
            file_content["t2_label"] = synset["t2_label"]
            file_content["job_description"] = synset["job_description"]
        file_list.append(file_content)
    return file_list


def train(input_dir: str, trn_splits: str, dev_splits: str, task: str, encoder: str, output_dir: str) -> str:
    trn_data = read_data(input_dir, trn_splits, task)
    dev_data = read_data(input_dir, dev_splits, task)
    model_path = os.path.join('{}-{}.torch'.format(task, output_dir))
    transformer = ECLAIRTransformer(task, encoder)
    transformer.train(trn_data, dev_data, output_dir=output_dir)
    transformer.save(model_path)
    return model_path


def decode(input_dir: str, tst_splits: str, task: str, model_path: str):
    count = 0
    correct = 0
    transformer = ECLAIRTransformer(model_path=model_path)
    for resume in read_data(input_dir, tst_splits, task):
        res = transformer.decode(resume)
        print(os.path.basename(model_path), res)
        if res["best"][0] == resume["t2_label"]:
            correct += 1
        count += 1
    print(correct, count)


if __name__ == '__main__':
    res_dir = "resources/splits_ref/"
    input_dir = "data/unanonymized"
    task = T2
    trn_split_file = res_dir + "{}-trn.json".format(task)
    dev_split_file = res_dir + "{}-dev.json".format(task)
    tst_split_file = res_dir + "{}-tst.json".format(task)
    encoder = 'roberta-large' if task == T1 else 'bert-large-cased'
    output_dir = 'test-model'

    model_path = train(input_dir, trn_split_file, dev_split_file, T2, encoder, output_dir)
    decode(input_dir, tst_split_file, T2, model_path)
