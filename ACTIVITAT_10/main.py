from fastapi import FastAPI
from services import word_services
from schemes.schemas import Option

app = FastAPI()

@app.get("/penjat/tematica/options", response_model=list[Option])
def get_themes():
    return word_services.get_themes()

@app.get("/penjat/tematica/{tematica}", response_model=list[Option])
def get_word(tematica: str):
    return word_services.get_random_word(tematica)