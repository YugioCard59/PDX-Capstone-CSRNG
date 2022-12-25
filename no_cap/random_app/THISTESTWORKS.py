# import glob
# import pandas as pd
# from pathlib import Path
# import numpy as np
# from json import dumps
# import json
# import math
# import bs4
# from bs4 import BeautifulSoup
# import csv
# import requests
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import sys
# # from PtQ6.QtGui import QApplication
# # from playwright.sync_api import sync_playwright
# import os
# import asyncio
# from pyppeteer import launch


# async def main():

#     browser = await launch()
#     page = await browser.newPage()
#     page_path = "file://" + os.getcwd() + "/templates/token_generation.html"
#     await page.goto(page_path)
#     page_content = await page.content()
#     soup = BeautifulSoup(page_content, 'html5lib')
#     print(soup.span)
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())


# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page_path = "file://" + os.getcwd() + "/templates/token_generation.html"
    
#     # page_path = Path.cwd().joinpath('templates', 'token_generation.html')
#     # print(page_path)
#     page.goto(page_path)
#     page_content = page.content()

#     soup = BeautifulSoup(page_content, 'html5lib')
#     print(soup.span)
#     browser.close()


# response = requests.get('http://127.0.0.1:8000/handle_csv')
# print(response.text)


# path = Path.cwd().joinpath('templates', 'token_generation.html').read_text()
# URL = "http://127.0.0.1:8000/templates/token_generation.html"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

# with open('templates/token_generation.html', 'r') as f:
#     contents = f.read()
#     soup = BeautifulSoup(contents, 'html5lib')
#     print(soup.span)

# url = "http://127.0.0.1:8000/handle_csv/"

# driver = webdriver.Chrome(Path.home().joinpath('Downloads', 'chromedriver'))
# driver.get(url)
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# all_divs = soup.find('span', {'id': 'writeToDom'})
# job_profiles = all_divs.find_all('hidden')
# print(all_divs)
# driver.close()



# path = "media/random_app"

# files = glob.glob(path + '/*.csv')
# data_frame = pd.DataFrame()
# content = []

# for filename in files:
#     df =  pd.read_csv(filename, index_col=None)
#     content.append(df)
# # ABOVE: for the row in csv containing only the label names
# # define this as content: a list where content[0] = pd's index col=None
# # bc there is no number for the first space, pd index start at data not labels
# # labels being strings is then concatenated to rest of df

# data_frame =  pd.concat(content)
# print(data_frame)

# '''ABOVE CODE WORKS
#     TESTING BELOW ##
#                     '''
# df_list = []
# for column in data_frame:
#     print(f"THIS COL: {data_frame[column]}")
#     for index in range(len(data_frame)):
#         # if data_frame[column][index].dtype.kind in 'iufc':
#         # print(type(f"THIS DATA IN COL: {data_frame[column][2]}"))
#         #     abs(data_frame[column][index])
#         df_list.append(data_frame[column][index])
# print(f"THIS DF as LIST: {df_list}")
# # print(f"THIS is LIST ELEMENT: {type(df_list[2])}") 
# # ABOvE element is numpy float


# remove_duplicates_set = set(df_list)
# print(remove_duplicates_set)

# # BELOW: is the list I want to pass to javascript
# clean_list = list(remove_duplicates_set) 
# print(clean_list)
# # print(type(clean_list[7]))


# # def cleanToInt(s):
# #     for element in range(len(clean_list)):
# #         # pandas .item method will iterate over column returns python scalar
# #         clean_list[element] = clean_list[element].item()
# #         if type(clean_list[element]) != float:
# #             clean_list[element] = float(clean_list[element])
# #         if clean_list[element] < 0:
# #             clean_list[element] = abs(clean_list[element])
# #         print(f"Try CHANGE numpy float to float and anything else to float: {type(clean_list[element])}")
# #     print(f"AFTER CLEAN and ABS: {type(clean_list)}")
# #     # HAVE to return list here for this to apply!!!
# #     clean_list_to_dict = {'clean_list': clean_list}
# #     print(f"DICT: {clean_list_to_dict}")
# #     return clean_list_to_dict
# #     # return clean_list
# # # print(f"TYPE of element after .item: {type(cleanToInt(clean_list)[2])}")
# # # print(f"ABS VAL try: {cleanToInt(clean_list)}")
# # print(cleanToInt(clean_list))


# # # def listToJson(s):
# # #     # This serializes (converts from complex data types to native data types) that can be converted to JSON where data can be stored and then transformed
# # #     dataJson = dumps(clean_list)
# # #     # ABOVE will turn python object to json string
# # #     print(type(dataJson))
# # #     print(f" this is data: {dataJson}")


# # # python_list = [-1.25, 2.0, 3.7, 4.99]
# # # json_string_list = dumps(python_list)
# # # print(json_string_list)

  








        






