from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    print(e)
if html is None:
    print("URL is not found")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
