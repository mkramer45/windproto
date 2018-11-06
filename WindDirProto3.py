import requests
from bs4 import BeautifulSoup

url = 'https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/'

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, 'lxml')

wind_directions = soup.find_all('td', {"class":"text-center last msw-js-tooltip td-square background-success"})

for w in wind_directions:
    print(w['title'])