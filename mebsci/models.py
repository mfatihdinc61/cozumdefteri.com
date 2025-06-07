from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class MebsciModel(AbstractUser):
    is_confirmed = models.BooleanField(default=False)
    donem = models.IntegerField(null=True, blank=True, help_text='')
    isim = models.CharField(max_length=100, null=True, blank=True, help_text='')
    soyisim = models.CharField(max_length=100, null=True, blank=True, help_text='')

    def __str__(self):
        return self.username