from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignUpView, Login

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
