from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.google.com').text
data = BeautifulSoup(html, 'lxml').prettify()
print(data)


