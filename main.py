from fastapi import FastAPI
from pydantic import BaseModel
import json

class Name(BaseModel):
    first_name: str
    last_name: str

app = FastAPI()

with open('db.json', 'r') as f:
    data = json.load(f)


@app.get("/names")
def read_names():
    return data

@app.get("/names/{id}")
def read_name(id: int):
    for persona in data["personas"]:
        if persona["id"] == id:
            return persona
    return {"error": "Name not found"}
