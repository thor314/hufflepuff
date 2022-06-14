from genericpath import isfile

from os import path

from click import FileError

from parser import remove_comments


IMPORT_KEYWORD = "include"
FILE_EXTENSION = ".puff"

class File:
    path: str
    content: str

class ReadFile:
    raw: str
    files: list[File]

    def __init__(self, raw, files):
        self.raw = raw
        self.files = files

def read_file(file: str) -> ReadFile:
    if not path.isfile(file):
        raise FileError("file doesn't exist")

    with open(file) as f:
        content = remove_comments(f.read())

    v = []
    while IMPORT_KEYWORD in content:
        idx_im = content.find(IMPORT_KEYWORD)
        if idx_im == 0:
            idx_nl_1 = 0
        else:
            idx_nl_1 = idx_im - str(reversed(content[:idx_im])).find("\n")

        idx_nl_2 = idx_im + content[idx_im:].find("\n")
        idx_nl_2 = len(content) if idx_nl_2 is -1 else idx_nl_2

        import_statement = str(content[idx_nl_1:idx_nl_2])
        content = str(content[idx_nl_2 + 1:]) if idx_nl_1 == 0 else str(
            content[:idx_nl_1 - 1]) + content[idx_nl_2 + 1:]

        import_statement = "\t\n ".split(import_statement.strip())
        # next_file = 

