from fastapi import APIRouter
from services import theme_services
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Theme(BaseModel):
    id: Optional[int]
    lang_id: str
    theme: str

@router.get("/theme/{lang_id}")
def get(lang_id: str):
    return theme_services.get_themes(lang_id.upper())

@router.post("/theme")
def post(theme: Theme):
    return theme_services.create_theme(theme)

@router.put("/theme")
def put(theme: Theme):
    return theme_services.update_theme(theme)

@router.delete("/theme/{id}")
def delete(id):
    return theme_services.delete(id)