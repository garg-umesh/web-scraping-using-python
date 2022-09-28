# Check README file for instructions

# Let us start coding

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL's
baseURL = 'https://www.thewhiskyexchange.com' # Change as per requirements
archiveURL = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=' # Change as per requirements

# Define variables and array's
productLinkList = []
singleProductDetailList = []
noOfPages = 2 # Change as per requirements

# Headers to be set with request
# User-Agent = Browser to be sent as request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

# Parse product URL's from archive pages including pagination pages
for x in range( 1, noOfPages+1 ):
    # Get archive page content
    r = requests.get( f' {archiveURL}{x} ', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    # Get products data
    archiveSingleProductBoxes = soup.find_all('li', class_ = 'product-grid__item')
     
    # Get Single product data
    for archiveSingleProductBox in archiveSingleProductBoxes:
        # Get Single Product URL and append with Base URL
        for productSinglePageURL in archiveSingleProductBox.find_all('a', href=True):
            productLinkList.append(baseURL + productSinglePageURL['href']) 
