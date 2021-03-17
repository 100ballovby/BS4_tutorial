from bs4 import BeautifulSoup
import requests

url = 'https://mignews.com'
page = requests.get(url)
print(page.status_code)

filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, 'html.parser')
allNews = soup.findAll('a', class_='time2', href=True)

for data in allNews:
    filteredNews.append(url + data['href'])


for data in filteredNews:
    print(data)