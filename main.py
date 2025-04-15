from fastapi import FastAPI

app = FastAPI(title="My FastAPI App")

@app.get("/")
def home():
    return {"message": "Hellow world"}