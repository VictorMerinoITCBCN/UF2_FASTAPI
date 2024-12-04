from fastapi import FastAPI
from services import lang_services, text_render_services, key_services, player_services

app = FastAPI()

@app.get("/languages")
def get_languages():
    return lang_services.get_languages()

@app.get("/text-render/{base}")
def get_text_render(base: str, lang_id: str):
    return text_render_services.get_text_render(base, lang_id.upper())

@app.get("/keyboard")
def get_keyboard(lang_id: str):
    return key_services.get_keys(lang_id.upper())

@app.get("/player")
def get_player(id: int):
    return player_services.get_player(id)