from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserRegistrationForm


def custom_register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hesap oluşturuldu, giriş yapabilirsin ama onaylanmadan gonderi yazamazsın/göremezsin, Fatih Komutanı bir dürt onaylasın seni')
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register3.html', {'form': form})


def custom_login(request):

    if request.user.is_authenticated:
        return redirect('gonderiler')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Böyle bir kullanıcı yok')
    return render(request, 'mainpage.html')