from django.db import models
from django.core.validators import FileExtensionValidator

class Csv_data(models.Model):
    file_name = models.FileField(upload_to='random_app', validators=[FileExtensionValidator(['csv'])])
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    def delete(self, *args, **kwargs):
        self.file_name.delete()
        self.upload_timestamp.delete()
        super().delete(*args, **kwargs)


    def __str__(self):
        return f"File id: {self.id}"

