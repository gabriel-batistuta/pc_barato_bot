from bs4 import BeautifulSoup
from requests import get
import json

def load_tree():
    with open('./mapping/tree.json', 'r') as f:
        data = json.load(f)
        return data

class Crawler():
    def __init__(self):
        self.tree = load_tree()
        self.url = ''

if __name__ == '__main__':
    load_tree()