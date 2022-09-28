# Check README file for instructions

# Let us start coding

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#URL's
baseURL = 'https://www.thewhiskyexchange.com' # Change as per requirements
archiveURL = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=' # Change as per requirements

# Define variables and array's
productLinkList = []
singleProductDetailList = []
noOfPages = 1 # Change as per requirements
#fileLocation = 'C:\Users\umesh\OneDrive\Documents'

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

# Parse data from Single product page
for singleLink in productLinkList:
    # Get Single Product page content
    r = requests.get(singleLink, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    # Get product details
    productName = (soup.find('h1', class_ = 'product-main__name').text.strip())
    productPrice = (soup.find('p', class_ = 'product-action__price').text.strip())
    try:
        productRating = (soup.find('span', class_ = 'review-overview__rating').text.strip())
    except:
        productRating = '0'

    # Add data into dictionary
    singleProductDetails = {
        'Name': productName,
        'Price': productPrice,
        'Rating': productRating
    }
    
    # Store all products data into list
    singleProductDetailList.append(singleProductDetails)

# Create Data Frame for products data
df = pd.DataFrame(singleProductDetailList)

# Create filename as dd-mm-YY H-M-S
dt_string = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

# Export Data Frame into CSV.
df.to_csv (fr'C:\Users\umesh\OneDrive\Documents\{dt_string}.csv',index=True, header=True)