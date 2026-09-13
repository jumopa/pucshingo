from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaotest():
    return {"teste": "deu certo"}
