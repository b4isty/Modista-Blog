from django.urls import path
from .views import home_page, CreateBlog, BlogList

app_name = 'blog'

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/create/', CreateBlog.as_view(), name='create'),
    path('blog/list/', BlogList.as_view(), name='list')
]