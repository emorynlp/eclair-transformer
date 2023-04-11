import json

from typing import List, Dict
from eclair.anonymize import *
from eclair.transformer import T1, T2

def read_split(file: str) -> Dict[str, List[int]]:
    """
    :param dir_path: the path of the json file containing resume IDs.
    :return: a dictionary of resume IDs for train, development, and test, respectively.
    """
    return json.load(open(file))

if __name__ == "__main__":
    tasks = [T1, T2]
    output_files_dir = "resources/"
    input_files_dir = "data/annotated/"
    field_reference = {"train": "/trn/", "development": "/dev/", "test": "/tst/"}
    processed_resumes = {}

    for task in tasks:
        split_dir = "resources/{}_splits.json".format(task)
        splits = read_split(split_dir)
        for split_field in splits:
            for resume_id in splits[split_field]:
                in_file_name = input_files_dir + str(resume_id) + '.json'
                out_file_name = output_files_dir + task + field_reference[split_field] + str(resume_id) + '.json'
                anonymized_resume = None
                if resume_id in processed_resumes:
                    anonymized_resume = processed_resumes[resume_id]
                else:
                    anonymized_resume = anonymize(json.load(open(in_file_name)))
                    processed_resumes[resume_id] = anonymized_resume
                with open(out_file_name, 'w') as outfile:
                    outfile.write(json.dumps(anonymized_resume))
                print(task, resume_id)
                