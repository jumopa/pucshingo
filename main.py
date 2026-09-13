from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}
async def funcaotest():
    return {"teste": True, "numero_aleatorio": random.randint(0, 1000)}
