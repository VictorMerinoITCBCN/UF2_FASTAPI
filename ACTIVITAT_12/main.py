from fastapi import FastAPI
import CRUD.key
import CRUD.language
import CRUD.player
import CRUD.text_render
import CRUD.theme
import CRUD.word
from services import lang_services, text_render_services, key_services, player_services, theme_services, word_services
import CRUD

app = FastAPI()

#CRUD
app.include_router(CRUD.language.router)
app.include_router(CRUD.player.router)
app.include_router(CRUD.key.router)
app.include_router(CRUD.text_render.router)
app.include_router(CRUD.theme.router)
app.include_router(CRUD.word.router)


@app.get("/languages")
def get_languages():
    return lang_services.get_languages()

@app.get("/text-render/{base}")
def get_text_render(base: str, lang_id: str = "en"):
    return text_render_services.get_text_render(base, lang_id.upper())

@app.get("/keyboard/{lang_id}")
def get_keyboard(lang_id: str = "en"):
    return key_services.get_keys(lang_id.upper())

@app.get("/player/{id}")
def get_player(id: int):
    return player_services.get_player(id)

@app.get("/themes/{lang_id}")
def get_themes(lang_id: str = "en"):
    return theme_services.get_themes(lang_id.upper())

@app.get("/words/{theme}/{lang_id}")
def get_words(theme: str, lang_id: str = "en"):
    return word_services.get_words(theme.upper(), lang_id.upper())

@app.get("/word/random/{theme}/{lang_id}")
def get_random_word(theme, lang_id: str = "en"):
    return word_services.get_random_word(theme.upper(), lang_id.upper())