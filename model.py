# model.py
from transformers import AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, AutoTokenizer

class Model:
  """A model class to lead the model and tokenizer"""

  def __init__(self) -> None:
    pass
  
  def load_model():
    model = AutoModelForSequenceClassification.from_pretrained("./models/roberta-base/")
    return model

  def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("./models/roberta-base/")
    return tokenizer