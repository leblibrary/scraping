import urllib.request
from bs4 import BeautifulSoup


quote_page = 'https://dev.intranet.leblibrary.com'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')



print(soup)