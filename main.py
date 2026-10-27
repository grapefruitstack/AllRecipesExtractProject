from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv 
from pathlib import Path
from ExtractContent import cuisinesDf

urls = cuisinesDf["url"].dropna().tolist()
response = requests.get(urls[0])
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)






# def get_sugar(url):

#     sugarList = []

#     response = requests.get(url)
#     soup_data = BeautifulSoup(response.text, "html.parser")
#     sugar_element = soup_data.find("span", {"class": "sugar"})
#     if sugar_element:
#         return sugar_element.text
#     return None

#     for url in urls:
#         sugar = get_sugar(url)
#         sugarList.append(sugar)



# print(sugarList)


# mm-recipes-nutrition-facts-label__table
# mm-recipes-nutrition-facts-label__table-body text-utility-300
# mm-recipes-nutrition-facts-label__nutrient-name mm-recipes-nutrition-facts-label__nutrient-name--has-postfix <- span
# "Total Sugars"
# ::after
# " ##g "

