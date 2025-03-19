from fastapi import FastAPI
from pathlib import Path
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = Path(__file__).resolve().parent.parent / "data.json"

@app.get("/data")
async def get_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    if not data:
        print("El archivo no es valido")

    return data


app.mount("/", StaticFiles(directory="/frontend/dist", html=True), name="frontend")
