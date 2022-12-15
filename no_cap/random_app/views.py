from django.shortcuts import render
from .forms import CsvForm
from django.http import HttpResponse
# from .models import Csv_data

# BELOW: this fnx will open and read file line by line where 
# UploadedFile.chunks() is safest read for memory

def upload_file(request):
    if request.method == 'POST':
        # form= is instantiating a csvform instance, file instance
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            # save() is attrib for modelForms won't work with just forms
            form.save()
            return render(request, 'token_generation.html')
    else:
            form = CsvForm()
        # below dict[name used in template: value] is what is being passed to html
    return render(request, 'welcome.html', {'form': form})

def token_generation(request):
    return render(request, 'token_generation.html')


# def handle_csv(request):
#     import glob
#     import pandas as pd
#     from pathlib import Path
#     import numpy as np
    
#     path = "media/random_app"

#     files = glob.glob(path + '/*.csv')
#     data_frame = pd.DataFrame()
#     content = []
#     for filename in files:
#         df =  pd.read_csv(filename, index_col=None)
#         content.append(df)
# # ABOVE: for the row in csv containing only the label names
# # define this as content: a list where content[0] = pd's index col=None
# # bc there is no number for the first space, pd index start at data not labels
# # labels being strings is then concatenated to rest of df
#     data_frame =  pd.concat(content)

#     df_list = []
#     for column in data_frame:
#     # print(data_frame[column])
#         for index in range(len(data_frame)):
#         # print(data_frame[column][index])
#             if data_frame[column][index] < 0 and type(data_frame[column][index] == int):
#                 data_frame[column][index] = abs(data_frame[column][index])
#             df_list.append(data_frame[column][index])

#     remove_duplicates_set = set(df_list)
# # BELOW: is the list I want to pass to javascript
#     clean_list = list(remove_duplicates_set) 
#     return render(request, 'token_generation.html', {'clean_list': clean_list})

def handle_csv(request):
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

    df_list = []
    for column in data_frame:
    # print(data_frame[column])
        for index in range(len(data_frame)):
            # print(type(data_frame[column][index]))
            if data_frame[column][index].dtype.kind in 'iufc':
                data_frame[column][index] = abs(data_frame[column][index])
            df_list.append(data_frame[column][index])

    remove_duplicates_set = set(df_list)
# BELOW: is the list I want to pass to javascript
    clean_list = list(remove_duplicates_set) 
    return render(request, 'token_generation.html', {'clean_list': clean_list})


           

                    