import requests
import bs4 
from bs4 import BeautifulSoup, SoupStrainer

 # print(bs4.__version__)

# r = requests.get('http://sfbay.craigslist.org/search/sss?query=motorcycles&sort=rel')
# raw_html = r.text
# # print(r.text)


# soup = BeautifulSoup(raw_html, 'html.parser')

# search_results = soup.find_all('a', {'class': 'i'})

# print(search_results[2]['href'])

example_listing ='http://seattle.craigslist.org/search/sss?query=macbook&sort=rel'

r = requests.get(example_listing)
ad_page_html = r.text

soup = BeautifulSoup(ad_page_html, 'html.parser')

listing = soup.find_all('a', {'class': 'result-title hdrlnk'})

print(listing)

# title = soup.find_all('h2', {'class': 'postingtitle'})

# print(title)

# search_results = soup.find_all('h2', {'class': ''})

# print(search_results)