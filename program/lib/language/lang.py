import locale

from program.lib.config.Config import cfg, Cfglib

if __name__ == "__init__":
    cur_lang = cfg.get(Cfglib.language)
    # if the language is not set, then set the language automatically according to the region
    # 如果当前语言未设置，则根据区域设置语言
    if cur_lang == "":
        cur_lang = locale.getdefaultlocale()[0]
        cfg.set(Cfglib.language, cur_lang)
