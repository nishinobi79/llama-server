from classifier import Classifier
from model import Model
from nlp import NLP

classifier = Classifier()
nlp = NLP(classifier)

print(type(classifier))

input_text = "Hi, i am good"
print("input_text:", input_text)
res = nlp.sentiment_analysis(input_text)

print(res)