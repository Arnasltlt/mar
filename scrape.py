import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://mariusvalaitis.tumblr.com/'

uClient = uReq(my_url)