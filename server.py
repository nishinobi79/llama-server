from fastapi import FastAPI
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/randomint")
async def root(x):
    return {"message": x}
