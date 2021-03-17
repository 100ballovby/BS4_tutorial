import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.findAll('span', class_='text')
authors = soup.findAll('small', class_='author')

q = {}
for author in authors:
    for quote in quotes:
        q[author.text] = quote.text

with open('quotes.json', 'w', encoding='utf-8') as f:
    f.write(str(q))
