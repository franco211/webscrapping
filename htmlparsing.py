'''search for tags by attributes, list of tags and parse tree navigation'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
namelist = bsObj.findAll("span", {"class": "green", "class": "red"});'''get a
list of all of the tags on the page'''
for name in namelist:
    print(name.get_text());  """separate content from the tags"""