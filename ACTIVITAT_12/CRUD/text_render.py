from fastapi import APIRouter
from services import text_render_services
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class TextRender(BaseModel):
    id: Optional[int]
    lang_id: str
    base: str
    text: str

@router.get("/text-render")
def get():
    return text_render_services.get_text_renders()

@router.post("/text-render/")
def post(text_render: TextRender):
    return text_render_services.create_text_render(text_render)

@router.put("/text-render/")
def put(text_render: TextRender):
    return text_render_services.update_text_render(text_render)

@router.delete("/text-render/{base}")
def delete(base: str):
    return text_render_services.delete_text_render(base)