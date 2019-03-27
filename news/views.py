from django.shortcuts import render

# Create your views here.

import requests

requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup

def scrape():
	session = requests.Session()
	session.headers = {"User Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
	url = 'https://www.theonion.com/'

	content = session.get(url, verify=False).content

	soup = BeautifulSoup(content, "html.parser")
	posts = soup.find_all('div',{'class':'curation-module__item'}) # returns a list
	print(len(posts))

	for i in posts:
		link = i.find_all('a',{'class': 'js_curation-click'})[1]
		image_source = i.find('img',{'class':'featured-image'})['data-src']
		print(link.text)
		print(image_source)
scrape()	

