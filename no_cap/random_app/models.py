from django.db import models
from django.utils.translation import gettext as _

class Csv_data(models.Model):
    # file_name will allow media folder to store uploaded files in a folder named random_app
    file_name = models.FileField(upload_to='random_app')
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

class Table_data(models.Model):
    table_name = models.CharField(max_length=100)
    fieldA = models.FloatField(_('fieldA'))
    fieldB = models.FloatField(_('fieldB'))
    # Enter method to delete entire table(uploaded file)

    def __str__(self):
        return f"{self.table_name}"