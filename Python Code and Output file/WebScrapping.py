#including the necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
import random

#function to create the generic search page URL
def GenerateSearchPageURL():
    searchPageURL = 'https://www.amazon.in/s?k='
    productName = input('Enter the name of the product: ')
    nameSplit = productName.split()
    first = True
    for i in nameSplit:
        if (first == True):
            searchPageURL = searchPageURL + i
            first = False
        else:
            searchPageURL = searchPageURL + '+' + i
    return searchPageURL



#using multiple user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
]
#declaring the headers for the http requests
headers = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-GB,en;q=0.5',
    'Dnt':'1',
    'Referer': 'https://google.com',
}


#Generating the URL for the specified project
URL = GenerateSearchPageURL()
print(URL)


#Sending the http request
r = requests.get(URL, headers = headers)
print(r.status_code)


soup= bs(r.content, 'html.parser')
links= soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal',
                    limit = 3)


amzUrl='https://www.amazon.in'
#page number
pn = 1
baseUrl = (amzUrl+links[2].get('href').strip()+'&reviewerType=all_reviews&pageNumber=').replace('dp', 'product-reviews')
#final URL for the review page of the product
finalUrl = baseUrl + str(pn)


#dictionaries to store the reviews
Dict={
    'reviews':[],
}


#sending actual http requests to the reviews page of the product
req = requests.get(finalUrl, headers = headers)


#actual web scrapping of the reviews
m = 1
while(req.status_code == 200):
    sop = bs(req.content, 'html.parser')
    parent = sop.find('div', id='cm_cr-review_list')
    Reviews = parent.find_all('span', class_='a-size-base review-text review-text-content')
    for k in Reviews:
        Dict['reviews'].append(k.text.strip())
    pn = pn + 1
    if (m>5):
        break
    finalUrl = baseUrl + str(pn)
    req = requests.get(finalUrl, headers= headers)
    print(req.status_code)
    time.sleep(2)
    m = m + 1


DataSet = pd.DataFrame(Dict)
print(DataSet.shape)
DataSet.to_excel("Reviews.xlsx")
