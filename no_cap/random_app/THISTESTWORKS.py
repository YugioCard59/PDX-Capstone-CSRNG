import glob
import pandas as pd
from pathlib import Path
import numpy as np
from json import dumps
import json
import math



path = "media/random_app"

files = glob.glob(path + '/*.csv')
data_frame = pd.DataFrame()
content = []

for filename in files:
    df =  pd.read_csv(filename, index_col=None)
    content.append(df)
# ABOVE: for the row in csv containing only the label names
# define this as content: a list where content[0] = pd's index col=None
# bc there is no number for the first space, pd index start at data not labels
# labels being strings is then concatenated to rest of df

data_frame =  pd.concat(content)
print(data_frame)

'''ABOVE CODE WORKS
    TESTING BELOW ##
                    '''
df_list = []
for column in data_frame:
    print(f"THIS COL: {data_frame[column]}")
    for index in range(len(data_frame)):
        # if data_frame[column][index].dtype.kind in 'iufc':
        print(type(f"THIS DATA IN COL: {data_frame[column][2]}"))
        #     abs(data_frame[column][index])
        df_list.append(data_frame[column][index])
print(f"THIS DF as LIST: {df_list}")
print(f"THIS is LIST ELEMENT: {type(df_list[2])}") 
# ABOvE element is numpy float


remove_duplicates_set = set(df_list)
print(remove_duplicates_set)

# BELOW: is the list I want to pass to javascript
clean_list = list(remove_duplicates_set) 
print(clean_list)
print(type(clean_list[7]))


def cleanToInt(s):
    for element in range(len(clean_list)):
        # pandas .item method will iterate over column returns python scalar
        clean_list[element] = clean_list[element].item()
        if type(clean_list[element]) != float:
            clean_list[element] = float(clean_list[element])
        if clean_list[element] < 0:
            clean_list[element] = abs(clean_list[element])
        print(f"Try CHANGE numpy float to float and anything else to float: {type(clean_list[element])}")
    print(f"AFTER CLEAN and ABS: {type(clean_list)}")
    # HAVE to return list here for this to apply!!!
    clean_list_to_dict = {'clean_list': clean_list}
    print(f"DICT: {clean_list_to_dict}")
    return clean_list_to_dict
    # return clean_list
# print(f"TYPE of element after .item: {type(cleanToInt(clean_list)[2])}")
# print(f"ABS VAL try: {cleanToInt(clean_list)}")
print(cleanToInt(clean_list))


def listToJson(s):
    # This serializes (converts from complex data types to native data types) that can be converted to JSON where data can be stored and then transformed
    dataJson = dumps(clean_list)
    # ABOVE will turn python object to json string
    print(type(dataJson))
    print(f" this is data: {dataJson}")


python_list = [-1.25, 2.0, 3.7, 4.99]
json_string_list = dumps(python_list)
print(json_string_list)

  








        






