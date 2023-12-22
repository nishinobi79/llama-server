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

@router.get("/")
async def home():
    return {"message": "Machine Learning service"}

@router.post("/generation")
async def data(data: dict):
    try:
        input_text = data["text"]
        res = nlp.text_generation(input_text)
        return {"res": res}
    except Exception as e:
        log.error("Something went wrong")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)