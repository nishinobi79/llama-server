from generator import Generator

class NLP:
    def __init__(self, generator:Generator):
        self.generator = generator

    def text_generation(self, text): 
        output = self.generator.get_generated_text(text)
        return output