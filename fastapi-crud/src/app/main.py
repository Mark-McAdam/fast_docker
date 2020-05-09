from fastapi import fastapi

app = FastAPI()

@app.get("/ping")
def pong():
    return{"ping": "pong!"}