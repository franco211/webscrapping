from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_Title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = get_Title("https://www.pythonscraping.com/exercises/exercise1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
