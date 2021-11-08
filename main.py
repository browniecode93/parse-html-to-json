import json
import xmltojson

from pathlib import Path
from bs4 import BeautifulSoup

def read_files_name(root):
    # Read all directories on data
    directories = [item for item in Path(root).iterdir() if Path(item).is_dir()]
    # Create file name
    for dir in directories:
        file_names = []
        print(f'Read files on {dir}')
        for f in Path(dir).iterdir():
            if f.suffix == '.html':
                file_names.append(f'{str(dir)}/{f.name}')
        if str(dir) != 'lot-parser/data/2017-12-20':
            print(dir)
            html2json(file_names)

def html2json(file_names):
    content = []
    for file in file_names:
        works = []
        # Check if file is empty
        if Path(file).stat().st_size != 0:
            with open(file, "r") as html_file:
                html = html_file.read()
                soup = BeautifulSoup(html, "html.parser")
                works.append({
                    "title": soup.find('h3').get_text(),
                    "price": soup.find_all('div')[1].get_text()
                })
                info = {
                    "artist": soup.find('h2').get_text(),
                    "works": works
                }
                content.append(info)

    json2file(f'{str(Path(file).parent)}/result.json', content)

def json2file(file_name, content):
    with open(file_name, "w") as file:
        json.dump(content, file)


if __name__ == "__main__":
    file_names = read_files_name('lot-parser/data/')
