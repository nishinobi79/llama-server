from classifier import Classifier

class NLP:
    def __init__(self, classifier:Classifier):
        self.classifier = classifier

    def sentiment_analysis(self, text): 
        sentiment = self.classifier.get_sentiment_label_and_score(text)
        return sentiment