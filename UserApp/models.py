from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    username=models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateField()
    updated_at=models.DateField()

    def __str__(self):
        return self.text
