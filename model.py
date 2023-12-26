# model.py
from transformers import AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, AutoTokenizer, AutoModelForCausalLM

class Model:
  """A model class to lead the model and tokenizer"""

  def __init__(self) -> None:
    pass
  
  def load_model():
    model = AutoModelForCausalLM.from_pretrained("./models/tweets-bloom-560m")
    return model

  def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("./models/tweets-bloom-560m")
    return tokenizer