from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Landing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
# Create your models here.
