from fastapi import FastAPI, APIRouter
import uvicorn
from generator import Generator
from model import Model
from nlp import NLP
import logging as log
import json
import numpy as np

log.basicConfig(level = log.INFO)

app = FastAPI()
router = APIRouter()
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


@router.get("/")
async def home():
    return {"message": "Machine Learning service"}

@router.post("/generation")
async def data(data: dict):
    try:
        input_text = data["text"]
        res = nlp.text_generation(input_text)
        res = extract_substring_between_backticks(res[0])
        res = eval(res)['response']
        return res

    except Exception as e:
        log.error("Something went wrong")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)