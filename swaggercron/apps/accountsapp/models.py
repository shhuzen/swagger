from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255,null=True)
    short_description = models.CharField(max_length=255,null=True)
    detailed_description = models.TextField(null=True)
    picture = models.ImageField(upload_to='media/accounts/pictures/',null=True,blank=True)