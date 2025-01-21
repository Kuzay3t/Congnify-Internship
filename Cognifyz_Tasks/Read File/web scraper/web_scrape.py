def line_break():
    print("*" * 50)

from bs4 import BeautifulSoup

with open("website.html") as file:
    website_content = file.read()
     
soup = BeautifulSoup(website_content, "html.parser" )
print(soup.title)
line_break()
print(soup.title.string)
line_break()
print(soup.title.tag)
line_break()
print(soup.prettify())