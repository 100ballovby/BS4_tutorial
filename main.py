from bs4 import BeautifulSoup
import requests

url = 'https://mignews.com/'
page = requests.get(url)
print(page.status_code)
