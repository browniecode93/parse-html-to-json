import json
import xmltojson

from pathlib import Path


def read_file_name(root):
    file_name = []
    # Read all directories on data
    directories = [item for item in Path(root).iterdir()]
    # Create file name
    for dir in directories:
        for f in Path(dir).iterdir():
            file_name.append(f'{str(dir)}/{f.name}')

    return file_name

def html2json():
    return

def print_json():
    return

if __name__ == "__main__":
    file_name = read_file_name('lot-parser/data/')
    print(file_name)