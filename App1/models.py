from django.db import models

# Create your models here.
class User_register(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    mobile=models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    class Meta:
        db_table="User Register"