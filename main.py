import json
import xmltojson

from pathlib import Path
from bs4 import BeautifulSoup

def check_if_in_list_of_dict(dict, value):
    """Check if given key exists in list of dictionaries """
    for elem in dict:
        if value in elem.values():
            return True
    return False


def create_json_without_html_class(soup, content):
    """Create a json from html file without class name in tags """
    works = []
    works.append({
        "title": soup.find('h3').get_text(),
        "currency": soup.find_all('div')[1].get_text().split(' ')[0],
        "price": soup.find_all('div')[1].get_text().split(' ')[1]
    })
    info = {
        "artist": soup.find('h2').get_text(),
        "works": works
    }
    content.append(info)
    return content


def create_json_with_html_class(soup, artist_dict):
    """Create a json from html file with class name in tags """
    works = []
    artist_name = soup.find('h3', attrs={'class': 'artist'}).get_text()
    if check_if_in_list_of_dict(artist_dict, artist_name):
        for item in artist_dict:
            if item['artist'] == artist_name:
                item['works'].append({
                    "title": soup.find_all('h3')[1].get_text(),
                    "currency": soup.find('span', attrs={'class': 'currency'}).get_text(),
                    "price": soup.find_all('span')[1].get_text()
                })
    else:
        works.append({
            "title": soup.find_all('h3')[1].get_text(),
            "currency": soup.find('span', attrs={'class': 'currency'}).get_text(),
            "price": soup.find_all('span')[1].get_text()
        })
        info = {
            "artist": soup.find('h3', attrs={'class': 'artist'}).get_text(),
            "works": works
        }
        artist_dict.append(info)
    return artist_dict


def json2file(file_name, content):
    """Write json object in each directory """
    with open(file_name, "w") as file:
        json.dump(content, file)


def html2json(file_names):
    """Create json for all files in a directory"""
    content = []
    for file in file_names:
        # Check if file is empty
        if Path(file).stat().st_size != 0:
            with open(file, "r") as html_file:
                html = html_file.read()
                soup = BeautifulSoup(html, "html.parser")
                if soup.find('h2'):
                    content = create_json_without_html_class(soup, content)
                else:
                    content = create_json_with_html_class(soup, content)
    json2file(f'{str(Path(file).parent)}/result.json', content)


def read_files_name(root):
    """Read all files in given directory """
    # Read all directories on data
    directories = [item for item in Path(root).iterdir() if Path(item).is_dir()]
    # Create file name
    for dir in directories:
        file_names = []
        print(f'Read files on {dir}')
        for f in Path(dir).iterdir():
            if f.suffix == '.html':
                file_names.append(f'{str(dir)}/{f.name}')
        html2json(file_names)


if __name__ == "__main__":
    read_files_name('lot-parser/data/')
