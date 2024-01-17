from fastapi import FastAPI

from pythonApi.lib.language.lang import lang

app = FastAPI()


@app.get("/lang/get/{lang_key}")
async def get_lang(lang_key):
    return lang.get(lang_key)

# while 1:
#     sleep(1000)
#     print("responding")
