from django.db import models

class Token_user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s" % (self.user_name)

class Token_storage(models.Model):
    token_value = models.CharField(max_length=200)
    token_user =  models.ForeignKey(Token_user, on_delete=models.CASCADE)

    def __str__(self):
        return self.token_value