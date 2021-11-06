#Importing the required modules 
# import os
# import sys
# import pandas as pd
# from bs4 import BeautifulSoup
   
# path = 'http://www.starbuckseverywhere.net/StoreOpeningDates.html'
# # empty list
# data = []
# # for getting the header from
# # the HTML file
# list_header = ["Starbucks opening dates"]
# soup = BeautifulSoup(open(path),'html.parser')
# header = soup.find_all("table")[0].find("tr")
  
# for items in header:
#     try:
#         list_header.append(items.get_text())
#     except:
#         continue
  
# # for getting the data 
# HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
  
# for element in HTML_data:
#     sub_data = []
#     for sub_element in element:
#         try:
#             sub_data.append(sub_element.get_text())
#         except:
#             continue
#     data.append(sub_data)
  
# # Storing the data into Pandas
# # DataFrame 
# dataFrame = pd.DataFrame(data = data, columns = list_header)
   
# # Converting Pandas DataFrame
# # into CSV file
# dataFrame.to_csv('starbucks.csv')


#Real Estate API

import requests

url = "https://realty-in-us.p.rapidapi.com/locations/auto-complete"

querystring = {"input":"Texas"}

headers = {
    'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
    'x-rapidapi-key': "ad9c006358msh99b8a6bd807e76fp182be9jsn32392df16ceb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#Yelp

import requests

url = "https://yelpapiserg-osipchukv1.p.rapidapi.com/getAutocomplete"

payload = "text=%3CREQUIRED%3E&accessToken=%3CREQUIRED%3E"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "YelpAPIserg-osipchukV1.p.rapidapi.com",
    'x-rapidapi-key': "ad9c006358msh99b8a6bd807e76fp182be9jsn32392df16ceb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)