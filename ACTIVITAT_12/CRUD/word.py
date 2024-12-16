from fastapi import APIRouter
from services import word_services
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Word(BaseModel):
    id: Optional[int]
    lang_id: str
    word: str
    theme_id: int

@router.get("/words")
def get():
    return word_services.get_all_words()

@router.post("/word")
def post(word: Word):
    return word_services.create_word(word)

@router.put("/word")
def put(word: Word):
    return word_services.update_word(word)

@router.delete("/word/{id}")
def delete(id: int):
    return word_services.delete_word(id)