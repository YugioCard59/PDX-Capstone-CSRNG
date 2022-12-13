# from .models import Csv_data

# def open_csv():
#     obj = Csv_data.objects.get()
#     with open(obj.file_name.path, 'wb+') as f:
#         for chunk in obj.file_name.path.chunks():
#             f.write(chunk)
#             print(chunk)

# print(open_csv())

import glob
import pandas as pd
import os
from pathlib import Path
# # print(Path.cwd())
# from django.db import models
# from .models import Csv_data

print(UploadedFile.chunks())


# path = os.path.join(BASE_DIR, 'media')

# files = glob.glob(path + '/*.csv')
# data_frame = pd.DataFrame()
# content = []

# for filename in files:
#     df =  pd.read_csv(filename, index_col=None)
#     content.append(df)

# data_frame =  pd.concat(content)
# print(data_frame)


# dir_name = 'C:\Users\isaco\Desktop\PDX-Capstone-CSRNG\no_cap\media\random_app'
# content = []
# for file in os.listdir(dir_name):
#     df =  pd.read_csv(file)
#     content.append(df)

# final_content = df.append(df for df in content)
# print(final_content)

# path =  Path(r'.')
# for filename in path.iterdir():
#     with filename.open() as f:
#         for chunk in filename.chunks():
#             f.write(chunk)
#             print(chunk)

# obj = Csv_data.objects.filter(file_name__endswith=".csv")
# with open(obj.file_name.path, 'wb+') as f:
#     for chunk in obj.file_name.path.chunks():
#         f.write(chunk)
#         print(chunk)