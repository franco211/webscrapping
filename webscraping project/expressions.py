from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# error handling
try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    print(e)
# if statement will check for server.
if html is None:
    print("Url not found")

# attribute error handling
try:
    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj.body.h1)
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent is None:
        print("Tag was not found")
    else:
        print(badContent)


