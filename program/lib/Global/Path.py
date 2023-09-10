import os.path


class Path:
    curdir = ""

    def __init__(self):
        self.curdir = os.path.dirname(os.path.abspath(__file__))
        self.curdir = self.acurdir("../../")

    def acurdir(self, path_: str):
        """
        returns the string of current path joined with the additional path\n
        返回一个包含当前python运行路径和参数path中路径拼接起来的字符串
        :param path_: the path which you want to be attached to the current path
        :return: the string of current path joined with the additional path
        """
        path_.replace("\\", "/")
        path_list = path_.split('/')
        cur_path = self.curdir.replace("\\", "/")
        cur_path_list = cur_path.split('/')
        pointer = len(cur_path_list)
        p_pointer = 0
        for item in path_list:
            if item == "..":
                pointer -= 1
                p_pointer += 1
            elif item == ".":
                p_pointer += 1
            else:
                break
        n_list = cur_path_list[:pointer] + path_list[p_pointer:]
        r_path = ""
        for item in n_list:
            r_path += item + r"/"
        return r_path.rstrip('/')


mapath = Path()
