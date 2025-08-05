from tkinter import filedialog
from pathlib import Path
from method import to_csv
import os
import platform
import subprocess


def open_folder(path):
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", path])
    else:  # Assume Linux
        subprocess.run(["xdg-open", path])


if __name__ == '__main__':
    _path = Path(filedialog.askopenfilename(title='Select a Waters XML Export'))
    to_csv(_path)
    open_folder(Path.cwd())
