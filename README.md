# eclair-transformer

## Installation

Python 3.7 or higher is recommended: 

```
pip install .
```

## Dataset Arrangement

### train

To train the model, arrange the data in the following structure:

```json
{
	"train": \
	[
		CV1,
		CV2,
		CV3,
		...
	],
	"eval": \
	[
		CV1,
		CV2,
		CV3,
		...
	]
}
```

where each CV is the structure below (must contain the specified fields):

```json
{
	"Qualification":"CONTENT",
	"Certification":"CONTENT",
	"Experience":"CONTENT",
	"JobProfile":"CONTENT",
	"t1_label":"T1_LABEL", // For T1 training
	"t2_label":"T2_LABEL", // For T2 training
	"job_description":"JOB_DESCRIPTION_CONTENT" // For T2 training
}
```

The recommended way of generating data in such structure is to generate each CV first in the following format with their resume ID as there name (`12345.json` for example):

```json
{
	"Qualification":"CONTENT",
	"Certification":"CONTENT",
	"Experience":"CONTENT",
	"JobProfile":"CONTENT",
}
```

and then create a splits file in the following json format:

```json
[
	{
		"resume_id":12345,
		"t1_label":"T1_LABEL", // If available
		"t2_label": "T2_LABEL", // If available
		"job_description": "JOB_DESCRIPTION_CONTENT" // If available
	}
	...
]
```

and merge the two fields to create resumes. For detailed implementation of data generation process as such please refer to [demo_transformer.py](https://github.com/emorynlp/eclair-transformer/blob/main/eclair/demo/demo_transformer.py)

### decode

To decode, arrange a single CV in as following:

```json
{
	"Qualification":"CONTENT",
	"Certification":"CONTENT",
	"Experience":"CONTENT",
	"JobProfile":"CONTENT",
	"job_description": "JOB_DESCRIPTION" // Necessary for T2 Training
}
```

## Initialization

Eclair-transformer need either a specified (task & encoder) or a specified model to work. For training purpose, both task and encoder have to be specified. For decoding purpose, the model to be used for decoding has to be specified.

* `task`: the task to run on the object. `T1`, or `"t1"` for **T1 tasks**, or multi-labeled competence level classification; `T2`, or `"t2"` for **T2 tasks**, or binary-labeled acceptance prediction.
* `encoder`: the type of tokenizer to use for training (or the type of the model for training or decoding). put a BERT structure tokenizer (`"bert-large-cased"`, for example) if using a BERT model or a RoBERTa structure tokenizer (`"roberta-large"`) if using a RoBERTa model.
* `model_path`: the path to the model file loaded upon initialization as the model for the object. 
* `output_dir`: the directory to store the checkpoint files generated during the training process.

## Train

The `train()` method takes in the training data and the development data and trains the model. 

To train the model, initialize the eclair-transformer with specified task and encoder

```python
task = T1
encoder = 'roberta-large'
transformer = ECLAIRTransformer(task, encoder)
```

 and then call on the `train()` method

```python
trn_data = "path/to/training/data"
dev_data = "path/to/development/data"
model_path = os.path.join('{}-model.torch'.format(task))
transformer.train(trn_data, dev_data)
```

## Decode

To generate the prediction of a resume using the tool, call the `decode()` method.

To decode a resume, initialize the eclair-transformer with specified model

```python
model_path = "path/to/model"
transformer = ECLAIRTransformer(model_path=model_path)
```

The method takes in one parameter:

* `resume`: the resume, in dictionary format, to be parsed.

```python
resume = json.load(open("path/to/resume"))
res = transformer.decode(resume)
print(res)
```

It is expected that for **T1** prediction the output should be something like:

```
[
  {
    "best_prediction": [
      [
        "CRCI",
        0.2707805931568146
      ]
    ],
    "predictions": {
      "NQ": 0.14438876509666443,
      "CRCI": 0.2707805931568146,
      "CRCII": 0.10479626059532166,
      "CRCIII": 0.2588427662849426,
      "CRCIV": 0.22119157016277313
    }
  }
]
```

And for **T2** prediction:

```
[
  {
    "best_prediction": [
      [
        "YES",
        0.8009408712387085
      ]
    ],
    "predictions": {
      "NO": 0.1990591585636139,
      "YES": 0.8009408712387085
    }
  }
]
```

