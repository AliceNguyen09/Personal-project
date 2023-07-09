# Web scraping with Python

## Introduction
This project scrape data from Amazon website and convert it into a csv file.<br/>
In particular, we want to get a list of all 'kindle paperwhite' on Amazon website. We want to extract the name of the product, price, rating, number of review, and the link to the product.<br/>
The script amazon_scraping.py is used to extract data from the website and turn it into a csv file.<br/>
The result file - amazon_data.csv - was produced on 16th July 2023.

## Process
### Step 1: Import libraries
```
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
```

### Step 2: Create connection
```
# The webpage URL
URL = 'https://www.amazon.com/s?k=kindle+paperwhite&crid=3THZ52TK2G2HA&sprefix=kind%2Caps%2C86&ref=nb_sb_ss_ts-doa-p_2_4'

# Headers for requests
HEADERS = ({'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15', 'Accept_language' : 'en-US, en;q=0.5'})

# HTTP request
webpage = requests.get(URL, headers= HEADERS)
```
### Step 3: Find the link of all tag objects
```
# Soup object containing all data
soup = bs(webpage.content, 'html.parser')

# Fetch links of all tag objects
links = soup.find_all('a', attrs={'class', 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

# Store the links
links_list = []

# Loop for extracting link from each object
for link in links:
    links_list.append(link.get('href'))
```

### Step 4: Find the data of each object
```
# Function to extract Product Title
def get_title(soup):
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

	except AttributeError:
		title_string = ""	
	return title_string

# Function to extract Product Price
def get_price(soup):
	try:
		price = soup.find("span", attrs={'class':'a-offscreen'}).text
	except AttributeError:
		price = ""	
	return price

# Function to extract Product Rating
def get_rating(soup):
	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
	except AttributeError:
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	
	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
	except AttributeError:
		review_count = ""	
	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()
	except AttributeError:
		available = ""	
	return available	
```

### Step 5: Turn all data into a csv file
```
d = {'title' : [], 'price' : [], 'rating' : [], 'review' : [], 'availability' : [], 'link': []}

# Loop for extracting details from each link
for link in links_list:
    new_webpage = requests.get('https://www.amazon.com' + link, headers=HEADERS)
    new_soup = bs(new_webpage.content, 'html.parser')

    # Display products information
    d['title'].append(get_title(new_soup))
    d['price'].append(get_price(new_soup))
    d['rating'].append(get_rating(new_soup))
    d['review'].append(get_review_count(new_soup))
    d['availability'].append(get_availability(new_soup))
    d['link'].append('https://www.amazon.com' + link)

# Save data into csv file
amazon_df = pd.DataFrame.from_dict(d)
amazon_df['title'].replace('', np.nan, inplace=True)
amazon_df = amazon_df.dropna(subset=['title'])
amazon_df.to_csv('amazon_data.csv', header=True, index=False)
```

In the final step, we exclude the rows with blank 'title' because those rows are meaningless.

## Result
We have a csv file containing the list of all kindle paparwhite on Amazon, with its price, rating, number of review, availability and the link to the product.