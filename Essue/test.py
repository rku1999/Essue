import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://money.cnn.com/data/markets/sandp/'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs = {'class':'wsod_fLeft'})
name = name_box.text.strip()
price_box = soup.find('span', attrs = {'stream':'last_575769'})
price = price_box.text.strip()

quote_page_2 = 'https://money.cnn.com/data/hotstocks/index.html'
page_2 = urllib2.urlopen(quote_page_2)

soup_2 = BeautifulSoup(page_2, 'html.parser')
name_box_2 = soup_2.find('a', attrs = {'class':'wsod_symbol'})
name_2 = name_box_2.text.strip()
price_box_2 = soup_2.find('span', attrs = {'stream':'last_599362'})
price_2 = price_box_2.text.strip()

name_box_3 = soup_2.find('a', attrs = {'href':'/data/markets/nasdaq'})
name_3 = name_box_3.text.strip()
price_box_3 = soup_2.find('span', attrs = {'stream':'last_579435'})
price_3 = price_box_3.text.strip()



print name,":",price
print name_2,":",price_2
print name_3,":",price_3