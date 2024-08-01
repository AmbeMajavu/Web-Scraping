#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://techcrunch.com/2024/07/31/india-is-the-largest-market-for-meta-ai-usage/"

# Sending a request to fetch the HTML content of the page
response = requests.get(url)

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the headline
headline = soup.find('h1').get_text()
print(headline)