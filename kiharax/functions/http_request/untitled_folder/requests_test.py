import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

# load_url = "https://en.wikipedia.org/wiki/Index"
load_url = "https://en.wikipedia.org/wiki/Name"
# load_url = "https://en.wikipedia.org/wiki/Age"
# load_url = "https://en.wikipedia.org/wiki/Gender"
# load_url = "https://en.wikipedia.org/wiki/Height"
# load_url = "https://en.wikipedia.org/wiki/Weight"
# load_url = "https://en.wikipedia.org/wiki/Description"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup.find("title").text)
# for element in soup.find_all("p"):
#     print(element.text)
print(soup)