# grab all tags in the html file.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
for tag in bsObj.findAll(True):
    print(tag.name)