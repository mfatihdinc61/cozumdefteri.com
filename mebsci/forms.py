from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MebsciModel


class CustomUserRegistrationForm(UserCreationForm):
    isim = forms.CharField(max_length=100, required=True)
    soyisim = forms.CharField(max_length=100, required=True)
    donem = forms.IntegerField(required=True)

    class Meta:
        model = MebsciModel
        fields = ['username', 'password1', 'password2', 'isim', 'soyisim', 'donem']
        labels = {
            'username': 'Kullanıcı Adı',
            'password1': 'Şifre',
            'password2': 'Şifre Doğrulama',
            'donem': 'Dönem',
            'soyisim': 'Soyisim',
        }
        help_texts = {
            'username': 'Zorunlu. 150 karakter ya da daha az. Sadece harf, rakam ve @/./+/-/_ karakterlerini '
                        'içerebilir.',
            'password1': 'En az 8 karakter içermelidir. Sık kullanılan bir şifre olmamalıdır.',
            'password2': 'Şifrenizi doğrulayın.',
        }

        error_messages = {
            'password1': {
                'too_short': 'Şifre en az 8 karakter içermelidir.',
                'password_too_common': 'Bu şifre sık kullanılan bir şifre. Lütfen farklı bir şifre deneyin.',
            },
            'password2': {
                'password_mismatch': 'Şifreler eşleşmiyor. Lütfen aynı şifreyi girin.',
            },
        }
