import locale
import subprocess

from lib.config.Config import cfg, Cfglib

is_zhCn = locale.getdefaultlocale()[0] == "zh_CN"

path = input("Enter the python path where you want to install:\n")
pip_path = path + "/Scripts/pip.exe"

pack_list = [
    "opencv-python",
    "PyQt5",
    "pyqt5-tools"
    "easyocr"
]

if __name__ == "__main__":
    for package in pack_list:
        print(f"now installing package {package}")
        runArgs = [pip_path, "install", package]
        if is_zhCn:
            runArgs += ["-i", cfg.read(Cfglib.pipInstallSource)]
        process = subprocess.run(runArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.stderr != "".encode():
            print(process.stdout)
            print(process.stderr)
            input("Press any key to continue")
