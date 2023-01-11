from django.db import models
from django.contrib.auth.models import User

class Token_user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s" % (self.user_name)

class Token_storage(models.Model):
    token_value = models.CharField(max_length=200)
    token_user =  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.token_value

