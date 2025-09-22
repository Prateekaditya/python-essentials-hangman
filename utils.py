import os

def clearscreen():
    command = "clear" if os.name == "posix" else "cls"
    os.system(command)