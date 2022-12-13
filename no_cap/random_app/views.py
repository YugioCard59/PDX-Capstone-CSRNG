from django.shortcuts import render
from .forms import CsvForm
from django.http import HttpResponse
from .models import Csv_data


# BELOW: this fnx will open and read file line by line where 
# UploadedFile.chunks() is safest read for memory

def upload_file(request):
    if request.method == 'POST':
        # form= is instantiating a csvform instance, file instance
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            # save() is attrib for modelForms won't work with just forms
            form.save()
            return HttpResponse('great')
    else:
            form = CsvForm()
 
        # below dict[name used in template: value] is what is being passed to html
    return render(request, 'welcome.html', {'form': form})

           
# def open_csv(obj):
#     obj = Csv_data.objects.get(activated=False)
#     with open(obj.file_name.path, 'wb+') as f:
#         for chunk in obj.file_name.path.chunks():
#             f.write(chunk)
#             print(chunk)
                    