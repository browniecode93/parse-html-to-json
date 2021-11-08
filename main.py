import json
import xmltojson

from pathlib import Path


def read_files_name(root):
    file_names = []
    # Read all directories on data
    directories = [item for item in Path(root).iterdir() if Path(item).is_dir()]
    # Create file name
    for dir in directories:
        for f in Path(dir).iterdir():
            file_names.append(f'{str(dir)}/{f.name}')

    return file_names

def html2json(file_names):
    for file in file_names:
        file_obj = Path(file)
        if file_obj.stat().st_size != 0:
            with open(file, "r") as html_file:
                html = html_file.read()
                json_ = xmltojson.parse(html)
                json2file(f'{str(file_obj.parent)}/{file_obj.stem}.json', json_)
        else:
            print(f'File {file_obj.name} is empty!')

def json2file(file_name, content):
    with open(file_name, "w") as file:
        json.dump(content, file)

if __name__ == "__main__":
    file_names = read_files_name('lot-parser/data/')
    html2json(file_names)