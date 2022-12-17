from django.shortcuts import render
from .forms import CsvForm
from django.http import HttpResponse
# from .models import Csv_data
from json import dumps

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

def handle_csv(s):
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
                abs(data_frame[column][index])
            df_list.append(data_frame[column][index])

    remove_duplicates_set = set(df_list)
# BELOW: is the list I want to pass to javascript
    clean_list = list(remove_duplicates_set)
    for element in range(len(clean_list)):
        clean_list[element] = clean_list[element].item()
        if type(clean_list[element]) != float:
            clean_list[element] = float(clean_list[element])
        if clean_list[element] < 0:
            clean_list[element] = abs(clean_list[element])
            # I MAY NEED TO CONVERT THIS LIST TO A DICT? HERE??
    clean_list_to_dict = {'clean_list': clean_list}
    return clean_list_to_dict 

def cleaned_handle_csv(request):
    # newJsonCleanList = {'jsonCleanList': jsonCleanList}
    jsonCleanList = dumps(handle_csv())
    # print(jsonCleanList)
    return render(request, 'token_generation.html', {'clean_list1': jsonCleanList})


    


           

                    