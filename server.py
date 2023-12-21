from fastapi import FastAPI
import random
import string

app = FastAPI()

def generate_random_string():
    N = 7 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    return res


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/randomstr")
async def root(x):
    response = generate_random_string()
    return {"message": response}
