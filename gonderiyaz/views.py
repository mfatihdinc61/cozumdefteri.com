from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# newly added modules to have cache module worked 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


from django.shortcuts import render, get_object_or_404
from .models import Post

User = settings.AUTH_USER_MODEL


@login_required
def gonderiler(request):
    posts = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts = posts.filter(title__icontains=query)

    if not query:
        query = ""
        posts = posts.order_by('-publish_date')

        # posts = Post.objects.all().order_by('-publish_date')
    
    # else:
    # # If query is empty, display posts in descending order of publish date
    #     query = ""
    #     posts = Post.objects.all().order_by('-publish_date')
        
    return render(request, 'gonderiler.html', {'posts': posts, 'query': query})


# @method_decorator(cache_page(30))  # newly added for testing method decorator
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender = request.user
            post.save()
            return redirect('login')  # Redirect to home page after post creation
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, sender=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})
