from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
# from .forms import ModelFormWithFileField
# from .models import ModelWithFileField
# from django.views.generic.edit import FormView
# from .forms import FileFieldForm
# import pandas as pd
from .forms import CsvForm, UploadFileForm, FileFieldForm

from .models import Csv_data
import csv

# def welcome(request):
#     df = pd.read_csv('/temp_csv/*')
#     return render (request, 'welcome.html')

# def upload_csvfile(request):
#     form = CsvForm(request.POST or None, request.FILES or None)
#     # 'form' is name to be used in template and form is the value defined above
#     if form.is_valid():
#         form.save()
#         form = CsvForm()
#     context = {
#         'form': form
#     }
#     obj = Csv_data.objects.get(activated=False)
#     with open(obj.file_name.path, 'r') as f:
#         reader = csv.reader(f)
#         for i, row in enumerate(reader):
#             if i==0:
#                 pass
#             else:
#                 print(row)
#             print(row)
#     obj.activated = True
#     obj.save()
#     return render(request, 'welcome.html', context)

# from <path> import handle_upload_file


# def upload_file(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#         else:
#             form = UploadFileForm()
#         return render(request, 'upload.html', {'form': form})

# def handle_uploaded_file(file_to_open):
#     with open(<'some/file/name.txt'>, 'wb+') as destination:
#         for chunk in file_to_open.chuncks():
#             destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form =  CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Csv_data.objects.get(activated=False)
#     with open(obj.file_name.path, 'r') as f:
#         reader = csv.reader(f)
#         for i, row in enumerate(reader):
#             if i==0:
#                 pass
#             else:
#                 print(row)
#             print(row)
#     obj.activated = True
#     obj.save()
            return HttpResponseRedirect('/success/url/')
        else:
            form = CsvForm()
        return render(request, 'welcome.html', {'form': form})

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ModelFormWithFileField(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#         else:
#             form = UploadFileForm()
#         return render(request, 'upload.html', {'form': form})

# class FileFieldFormView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'
#     success_url: <insert URL or reverse()>
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for file in files:
#                 # TODO: what file is to todo
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
