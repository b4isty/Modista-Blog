from django.urls import path

from .views import home_page, CreateBlog, BlogList, SearchView, MyBlogs, BlogUpdateView, DeleteBlog

app_name = 'blog'

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/create/', CreateBlog.as_view(), name='create'),
    path('blog/list/', BlogList.as_view(), name='list'),
    path('blog/search/', SearchView.as_view(), name='search'),
    path('my-blog/', MyBlogs.as_view(), name='myblog'),
    path('my-blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('my-blog/delete/<int:pk>/', DeleteBlog.as_view(), name='delete'),
]
