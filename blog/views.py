from django.shortcuts import render, redirect
from django.views.generic import CreateView

from blog.forms import BlogCreateForm
from blog.models import Post


def home_page(request):
    """Function for home page"""
    if request.user.is_authenticated:
        return render(request, 'base.html')
    else:
        return redirect('users:login')

