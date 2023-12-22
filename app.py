from fastapi import FastAPI, APIRouter
import uvicorn
from classifier import Classifier
from model import Model
from nlp import NLP
import logging as log
import json
import numpy as np

log.basicConfig(level = log.INFO)

app = FastAPI()
router = APIRouter()
classifier = Classifier()
nlp = NLP(classifier)

@router.get("/")
async def home():
    return {"message": "Machine Learning service"}

@router.post("/sentiment")
async def data(data: dict):
    try:
        input_text = data["text"]
        print(input_text)
        res = nlp.sentiment_analysis(input_text)
        return {"res": res}
    except Exception as e:
        log.error("Something went wrong")

@router.post("/random")
async def data(data: dict):
    try:
        res = np.random.uniform(0,1)
        return {"res": res}
    except Exception as e:
        log.error("Something went wrong")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)