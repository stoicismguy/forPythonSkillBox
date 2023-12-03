from bs4 import BeautifulSoup
import requests
url = "http://www.columbia.edu/~fdc/sample.html"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
soup_find = soup.find_all('h3')
result = []
for element in soup_find:
    result.append(element.text.strip())

print(result)
