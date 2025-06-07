from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Post
        fields = ['title', 'recipient_type', 'post_type', 'content']
        labels = {
            'title': 'Başlık',
            'recipient_type': 'Gönderi Konusu',
            'post_type': 'Gönderi Tipi',
            'content': 'İçerik',
        }
