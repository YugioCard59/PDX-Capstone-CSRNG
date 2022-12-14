import glob
import pandas as pd
from pathlib import Path
import numpy as np

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
    # print(data_frame[column])
    for index in range(len(data_frame)):
        # print(data_frame[column][index])
        if data_frame[column][index] < 0 and type(data_frame[column][index] == int):
            data_frame[column][index] = abs(data_frame[column][index])
        df_list.append(data_frame[column][index])
print(df_list)

remove_duplicates_set = set(df_list)
print(remove_duplicates_set)

# BELOW: is the list I want to pass to javascript
clean_list = list(remove_duplicates_set) 
print(clean_list)
        






