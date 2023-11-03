import locale
from typing import TextIO

from pythonApi.lib.Global.Path import mapath
from pythonApi.lib.config.Config import cfg, Cfglib


class Lang:
    langList = {}

    def __init__(self):
        cur_lang = cfg.get(Cfglib.language)
        # if the language is not set, then set the language automatically according to the region
        # 如果当前语言未设置，则根据区域设置语言
        if cur_lang is None or cur_lang == "":
            cur_lang = locale.getdefaultlocale()[0].lower()
            cfg.set(Cfglib.language, cur_lang)
            cfg.save()

        lang_file = mapath.acurdir(f"./lang/{cur_lang}.lang")
        en_lang_file = mapath.acurdir(f"./lang/en_us.lang")
        file_handle = open(lang_file, "r")
        en_file_handle = open(en_lang_file, "r")
        # read en_us first
        # 先读取英文语言文件
        self._read_filehandle(en_file_handle, "ma")
        # then read other lang file, it will automatically replace the value in en_us lang list
        # 再读取其他语言的文件，这样即使其他语言文件存在缺失部分，也会默认显示英文
        if cur_lang != "en_us":
            self._read_filehandle(file_handle, "ma")
        en_file_handle.close()
        file_handle.close()

    def _read_filehandle(self, handle: TextIO, addition: str = ""):
        """
        read values from lang file handle into langList\n
        从语言文件句柄中读取键值对到langList中
        :param handle: lang file handle; 语言文件句柄
        :param addition: the addition before the key; 在key值前添加的额外内容
        :return: None
        """
        for line in handle.readlines():
            line_spilt = line.split('=')
            if len(line_spilt) <= 1:
                # todo warn missing value or key-value pair when reading given lang file
                pass
            name = f"{addition}.{line_spilt[0].strip()}"
            value = line_spilt[1].strip()
            self.langList[name] = value
        return None

    def add(self, module_name: str, lang_file: str):
        """
        add lang data from lang file, needs the module name you want to register\n
        从语言文件中读取数据，需要提供注册数据的模块名称
        :param module_name: the module name
        :param lang_file: the lang file
        :return: None
        """
        lang_file_handle = open(lang_file, "r")
        self._read_filehandle(lang_file_handle, module_name)
        lang_file_handle.close()

    def get(self, index: str) -> str:
        """
        Obtain corresponding language data based on the index\n
        When the data cannot be reached, returns "missing lang value"\n
        根据索引获得相应的语言数据，当数据索引不到时，返回"missing lang value"
        :param index: the index; 索引
        :return: str: the language data; 语言数据
        """
        if index not in self.langList.keys():
            # todo warn cannot find value pair to {index}
            return "missing lang value"
        return self.langList.get(index)


lang = Lang()
