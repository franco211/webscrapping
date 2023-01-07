from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
allText = bsObj.findAll(id = "text"); """bsObj.findAll("", {"id":"text"}) output the same """
print(allText[0].get_text())

"""namelist = bsObj.find(text = "the prince")"""
"""print(namelist)"""