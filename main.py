from generator import Generator
from model import Model
from nlp import NLP
import json

generator = Generator()
nlp = NLP(generator)


def extract_substring_between_backticks(input_string):
    start_index = input_string.find('{')  # Find the first occurrence and move to the character after ```
    end_index = input_string.find('}', start_index)+1  # Find the second occurrence starting from the first occurrence

    if start_index != -1 and end_index != -1:
        result = input_string[start_index:end_index].strip()
        return result
    else:
        return None  # Return None if either of the occurrences is not found


input_text = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nCategorize the given Input below into one of the 3 categories:\nPositive\nNegative\nNeutral\nGive the output in the json format.\n\nInput:\nI am going to do some really wholesome things for you and our community brother. get it?\n\n### Response:\n"
# print("input_text:", input_text)
res = nlp.text_generation(input_text)

res = extract_substring_between_backticks(res[0])
res = eval(res)["response"]

print(res)