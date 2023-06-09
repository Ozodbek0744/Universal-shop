from email.errors import MultipartInvariantViolationDefect
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from accounts.models.country import CountryModel
from avtoelon import settings
from uuid import uuid4

def upload_location(instance, filename):
    ext=filename.split('.')[-1]
    file_path= 'ads/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path

class AdPicturModel(models.Model):
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True)

class AdModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ads', on_delete=models.SET_NULL, blank=True, null=True)
    picture = models.ForeignKey(AdPicturModel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField()
    state = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    model = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    seen = models.IntegerField()
    ram = models.IntegerField()
    memory = models.IntegerField()
    dicount_price = models.IntegerField()
    
    def __str__(self):
        return str(self.model)

class FavAdModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='favs', on_delete=models.SET_NULL, blank=True, null=True)
    ad = models.ForeignKey(AdModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.owner} - {self.ad}"

