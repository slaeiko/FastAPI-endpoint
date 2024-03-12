from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

with open('db.json', 'r') as f:
    data = json.load(f)

    html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/names">/Nombres</a></li>
                <li><a href="/names/1">/Nombre, Id: 1</a></li>
                <li><a href="/names/2">/Nombre, Id: 2</a></li>
                <li><a href="/names/3">/Nombre, Id: 3</a></li>
            </ul>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get("/names")
def read_names():
    return data

@app.get("/names/{id}")
def read_name(id: int):
    for persona in data["personas"]:
        if persona["id"] == id:
            return persona
    return {"error": "Name not found"}
