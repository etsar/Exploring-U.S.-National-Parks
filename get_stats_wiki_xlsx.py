# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:36:17 2023

@author: entsa
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table on the page by its class or other attributes
    # You may need to inspect the HTML source of the page to determine the appropriate attributes
    table = soup.find("table", {"class": "wikitable"})

    # Use pandas to read the HTML table and convert it to a DataFrame
    df = pd.read_html(str(table))[0]

    # Save the DataFrame as an XLSX file
    df.to_excel("national_parks.xlsx", index=False)

    print("Table data saved as national_parks.xlxs")

else:
    print("Failed to retrieve the webpage.")
