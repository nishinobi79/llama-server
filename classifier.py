from scipy.special import softmax
from model import Model
import numpy as np
import torch
from torch import nn

class Classifier:
    def __init__(self):
        self.model = Model.load_model()
        self.tokenizer = Model.load_tokenizer()

    def get_sentiment_label_and_score(self, text: str):
        # X = torch.rand(1, 28, 28)
        # logits = model(X)
        # pred_probab = nn.Softmax(dim=1)(logits)
        # y_pred = pred_probab.argmax(1)

        # return y_pred

        result = {}
        labels = ["Negative", "Neutral", "Positive"]
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        result["label"] = str(labels[ranking[0]])
        result["score"] = np.round(float(scores[ranking[0]]), 4)
        return result