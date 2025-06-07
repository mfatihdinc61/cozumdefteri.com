from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from gonderiyaz.models import Post
from mebsci.models import MebsciModel

@login_required
def profil(request):
    user = request.user
    post_count = Post.objects.filter(sender=user).count()
    return render(request, 'profile.html', {'user': user, 'post_count': post_count})


