import glob
import json
import os

from eclair.transformer import ECLAIRTransformer, T1, T2


def read_data(dir_path: str):
    """
    :param dir_path: the path of the directory containing resume files in JSON.
    :return:
    """
    return [json.load(open(filename)) for filename in glob.glob(os.path.join(dir_path, '*.json'))]


def train(trn_path: str, dev_path: str, task: str, encoder: str, output_dir: str) -> str:
    trn_data = read_data(trn_path)
    dev_data = read_data(dev_path)
    model_path = os.path.join('{}-{}.torch'.format(task, output_dir))
    transformer = ECLAIRTransformer(T1, encoder)
    transformer.train(trn_data, dev_data, output_dir=output_dir)
    transformer.save(model_path)
    return model_path


def decode(tst_path: str, model_path: str):
    transformer = ECLAIRTransformer(model_path=model_path)
    for resume in read_data(tst_path):
        res = transformer.decode(resume)
        print(os.path.basename(model_path), res)


if __name__ == '__main__':
    trn_path = 'resources/trn'
    dev_path = 'resources/dev'
    tst_path = 'resources/tst'
    output_dir = '/local/scratch/bzhao44/ECLAIR/res/output'

    # T1: training and decoding
    encoder = 'roberta-large'
    model_path = train(trn_path, dev_path, T1, encoder, output_dir)
    decode(tst_path, model_path)

    # T2: training and decoding
    encoder = 'bert-large-cased'
    model_path = train(trn_path, dev_path, T2, encoder, output_dir)
    decode(tst_path, model_path)
