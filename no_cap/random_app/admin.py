from django.contrib import admin

from .models import Csv_data, Table_data

#REGISTER EACH MODEL HERE

admin.site.register(Csv_data)
admin.site.register(Table_data)
