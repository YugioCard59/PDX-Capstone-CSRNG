import glob
import pandas as pd
from pathlib import Path

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

# for val in data_frame[1]:
#     print(val)    

for column in data_frame:
    for i in range(len(data_frame)):
        if data_frame[column][i] != data_frame[column][i+1]:
            print(data_frame[column].values)
            print(type(data_frame[column]))
            print(type(data_frame[column][2]))
            print(type(data_frame[column].values))
            
        break




