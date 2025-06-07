from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from cozumdefteri.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient_type = models.CharField(max_length=50, choices=(
        ('Sisoft', 'Sisoft'),
        ('Terminal', 'Terminal'),
        ('Bilgisayar', 'Bilgisayar'),
        ('Kamera', 'Kamera'),
        ('Telefon', 'Telefon'),
        ('Yazıcı', 'Yazıcı'),
        ('Diğer - MEBS', 'Diğer - MEBS'),
        ('Diğer - MEBS DIŞI', 'Diğer - MEBS DIŞI'),
    ), default='Sisoft', blank=False, null=False)

    post_type = models.CharField(max_length=20, choices=(
        ('İşlem', 'İşlem'),
        ('Arıza Çözüm', 'Arıza Çözüm'),
        ('Teori', 'Teori')
    ), default='İşlem', blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)  # Add this line


    def __str__(self):
        return self.title
