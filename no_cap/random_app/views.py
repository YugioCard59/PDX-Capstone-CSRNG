from django.shortcuts import render, redirect
from .forms import CsvForm
from json import dumps
import os
from greenhouse_app.models import Token_storage

def upload_file(request):
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            # save() is attrib for modelForms won't work with just forms
            form.save()
            return render(request, 'token_generation.html')
    else:
        form = CsvForm()
        
        if request.method == 'GET' and '/login_home/' not in request.path_info:
            dir = './media/random_app/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

    path = "./static/cleanedList.json"
    isFile = os.path.isfile(path)
    print(f"from upload view does json exist: {isFile}")
    if isFile:
        os.remove(path)  
    return render(request, 'welcome.html', {'form': form})


def token_generation(request):
    return render(request, 'token_generation.html')


def handle_csv(request):
    import glob
    import pandas as pd
    
    path = "media/random_app"
    files = glob.glob(path + '/*.csv')
    data_frame = pd.DataFrame()
    content = []
    for filename in files:
        df = pd.read_csv(filename, index_col=None)
        content.append(df)
# # ABOVE: for the row in csv containing only the label names
# # define this as content: a list where content[0] = pd's index col=None
# # bc there is no number for the first space, pd index start at data not labels
# # labels being strings is then concatenated to rest of df
    data_frame = pd.concat(content)

    df_list = []
    for column in data_frame:
        for index in range(len(data_frame)):
            if data_frame[column][index].dtype.kind in 'iufc':
                abs(data_frame[column][index])
            df_list.append(data_frame[column][index])
 
    remove_duplicates_set = set(df_list)

    clean_list = list(remove_duplicates_set)
    for element in range(len(clean_list)):
        clean_list[element] = clean_list[element].item()
        if type(clean_list[element]) != float:
            clean_list[element] = float(clean_list[element])
        if clean_list[element] < 0:
            clean_list[element] = abs(clean_list[element])

    jsonCleanList = dumps(clean_list)
    jsonFile = open("./static/cleanedList.json", "w")
    jsonFile.write(jsonCleanList)
    jsonFile.close()

    if request.method == "POST" and request.user.is_authenticated:
        getHash = request.POST['writeToDom']
        new_token_form = Token_storage(token_value=getHash, token_user=request.user)
        new_token_form.save()

        dir = './media/random_app/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        path = "./static/cleanedList.json"
        isFile = os.path.isfile(path)
        print(f"json file exists? {isFile}")
        if isFile:
            os.remove(path)
            return redirect('greenhouse_app:show_seedling')

    return render(request, 'token_generation.html')







