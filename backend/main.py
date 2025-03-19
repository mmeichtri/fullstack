from fastapi import FastAPI, HTTPException
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
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data:
            raise HTTPException(status_code=400, detail="El archivo está vacío o no es válido.")

        return data

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo data.json no fue encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")


app.mount("/", StaticFiles(directory="/frontend/dist", html=True), name="frontend")
