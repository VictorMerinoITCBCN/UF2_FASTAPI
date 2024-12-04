from fastapi import FastAPI
from services import lang_services, text_render_services, key_services, player_services, theme_services, word_services

app = FastAPI()

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