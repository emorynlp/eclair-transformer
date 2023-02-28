# eclair_transformer

## Installation

Python 3.7 or higher is recommended: 

```
pip install .
```

## Dataset Arrangement

For a dataset example please refer to `tests/demo_multi.py` for **T1** and `tests/demo_binary.py` for **T2**.

### train

To train the model, arrange the data in the following structure:

```
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

```
{
  "Qualification":"CONTENT",
  "Certification":"CONTENT",
  "Experience":"CONTENT",
  "JobProfile":"CONTENT",
  "Label":"LABEL"
}
```

For **T2** training, the `JobDescription` section is necessary.

### decode

To decode, arrange a single CV in as following:

```
{
  "Qualification":"CONTENT",
  "Certification":"CONTENT",
  "Experience":"CONTENT",
  "JobProfile":"CONTENT",
}
```

For **T2** decoding, the `JobDescription` section is necessary.

## Initialization

The constructor takes in 3 parameters:

* `model_name`: the name of the model loaded upon initialization as the model for the object. Default set as a `from_pretrained` model from Huggingface based on the input `type`.
* `task`: the task to run on the object. `1` for **T1**, or multi-labeled competence level classification; `2` for **T2**, or binary-labeled acceptance prediction. (set as `1` by default)
* `type`: the type of model to use for training (or the type of the model loaded into ECLAIR). put `'bert'` for BERT or `'roberta'` for RoBERTa. (set as `'bert'` by default)

Call the python constructor to initiate ECLAIR as an object:

```python
from eclair_transformer.eclair import ECLAIR
ec = ECLAIR(model_name=None, task=1, type='bert')
```

## Train

To train the model, call on the `train()` method.

The method takes in 3 parameters:

* `dataset`: the dataset to be used in the training process
* `lr`: learning rate used for training, default as `2e-5`.
* `epochs`: epochs of training, default as `3`.

```python
ec.train(demo_dataset)
```

## Decode

To generate the prediction of a resume using the tool, call the `decode()` method.

The method takes in one parameter:

* `s`: the resume, in dictionary format, to be parsed.

```python
ec.decode(demo_resume)
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

