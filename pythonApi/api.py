from fastapi import FastAPI

from program.lib.language.lang import lang

app = FastAPI()


@app.get("/lang/get/{lang_key}")
async def get_lang(lang_key):
    return lang.get(lang_key)
