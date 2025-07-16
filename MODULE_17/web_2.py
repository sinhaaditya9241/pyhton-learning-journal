import requests 
from bs4 import BeautifulSoup


def Extract(url):
    response = requests.get(url = url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup

Extract(url = "https://en.wikipedia.org/wiki/Main_Page")
