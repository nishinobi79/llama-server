from scipy.special import softmax
from model import Model
import numpy as np
import torch
from torch import nn

class Generator:
    def __init__(self):
        self.model = Model.load_model()
        self.tokenizer = Model.load_tokenizer()

    def get_generated_text(self, text: str):        
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model.generate(input_ids=encoded_input['input_ids'],
                                     attention_mask=encoded_input['attention_mask'],
                                     renormalize_logits=False, do_sample=True,
                                     use_cache=True, max_new_tokens=10)
        result = self.tokenizer.batch_decode(output, skip_special_tokens=True)
        return result