import bs4
import requests
from bs4 import BeautifulSoup as soup
import sqlite3
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#list of URLs to scrape from
my_url = ['https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/']
# opening up connecting, grabbing the page

# conn = sqlite3.connect('SurfSend.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS WindInfo(ID INTEGER PRIMARY KEY, WindMPH TEXT)')

#iterate over list of URLS
for url in my_url:
	#initiating python's ability to parse URL
	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	#beautifulsoup magic
	page_soup = soup(page_html, "html.parser")
	#variable for soon to be parsed page
	wind = page_soup.findAll('td', class_=re.compile("text-center last msw-js-tooltip td-square background-success"))
	#prints the list of URLs we scraped from

# iterates over parsed HTML
	for w in wind:
		#wavesize
		title= (w.get('title data-original-title'))
		print(title)
