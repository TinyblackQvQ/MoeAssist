from enum import Enum

from program.lib.Global.Path import mapath


class ICfglib(Enum):
    ...


class Cfglib(ICfglib):
    pipInstallSource = "int"
    language = "str"


class Config:
    filePath = ""
    fileHandle = None
    cfglib = None
    list = {}

    def __init__(self, file_path=mapath.acurdir("../config.cfg"), cfglib=Cfglib):
        self.filePath = file_path
        self.cfglib = cfglib

    def update(self):
        """
        Update configurations from the config.cfg\n
        从配置文件中更新配置
        :return: None
        """
        self.fileHandle = open("r", self.filePath)
        for line in self.fileHandle.readlines():
            if line[0] == '#':
                continue
            split = line.split('=')
            name = split[0].strip()
            if len(split) == 1:
                value = None
            else:
                value = split[1].strip()
            for cfg_ in self.cfglib:
                if cfg_.name == name:
                    if value is None:
                        pass
                    elif cfg_.value == "float":
                        value = float(value)
                    elif cfg_.value == "bool":
                        value = bool(value)
                    elif cfg_.value == "int":
                        value = int(value)
                    self.list[cfg_] = value
                    break
            # todo raise warn unexpected cfg_ attr
        self.fileHandle.close()

    def save(self):
        """
        Save the cfgs in mem into the cfg file\n
        将当前内存中的配置保存至配置文件中
        :return: None
        """
        self.fileHandle = open("w", self.filePath)
        for item in self.list.keys():
            line = f"{item.name}={self.get(item)}\n"
            self.fileHandle.write(line)
        self.fileHandle.flush()
        self.fileHandle.close()

    def get(self, name: ICfglib):
        """
        To get the config value\n
        when one config's value is empty, it returns None\n
        获取某项配置的值。当某项配置的值为空，返回None
        :param name: the config enum instance; 配置的枚举类实例
        :return: Any; 任意值
        """
        return self.list[name]

    def set(self, config: ICfglib, value):
        """
        To set the config value\n
        设置某项配置的值
        :param config: the config enum instance; 配置的枚举类实例
        :param value: Any; 任意值
        :return: None
        """
        if str(type(value)).find(config.value) == -1:
            # todo raise error invalid value type
            pass
        self.list[config] = value


cfg = Config()
