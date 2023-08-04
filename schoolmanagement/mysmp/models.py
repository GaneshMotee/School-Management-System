from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gpm(models.Model):
    school_name=models.CharField(max_length=200)
    school_id=models.IntegerField()
    teachers=models.IntegerField()
    students=models.IntegerField()
    school_address=models.TextField(max_length=200)
    user= models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    
    
    
    
