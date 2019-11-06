from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
User = get_user_model()


class SignUpView(CreateView):
    """ View for Signup """
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        """ Overriding dispatch method to redirect authenticated user to login page """
        if self.request.user.is_authenticated:
            return redirect('/login')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


class Login(LoginView):
    """ View for Login """
    model = User
    template_name = 'users/login.html'
    success_url = '/blog/list/'

    def get(self,request, *args, **kwargs):
        """Overriding get method to redirect authenticated user to home page"""
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(Login, self).get(request, *args, **kwargs)

