from cgitb import html
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# first row of the table
# print(bsObj.find("table", {"id": "giftList"}).tr.)
# print(bsObj.table.tr)
# print(bsObj.tr)

# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)
#     '''prints out the list of product rows in the giftList
#    table.'''

# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     """previous_siblings function can also be used"""
#     print(sibling)
#     '''print all rows of products from the product table, except for the first title row.'''

# print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#
# for descendant in bsObj.find("table", {"id": "giftList"}).descendants:
#     print(descendant)


# grab URLs to all the product images
for image in bsObj.findAll("img"):
    print(image)