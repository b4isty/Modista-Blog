from django.contrib.auth import mixins
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from blog.models import Post
from blog.serializers import SearchResponseSerializer


def home_page(request):
    """Function for home page"""
    if request.user.is_authenticated:
        return redirect('blog:list')
    return redirect('users:login')


class CreateBlog(mixins.LoginRequiredMixin, CreateView):
    """
    View for creating blog
    """
    model = Post
    fields = ['title', 'content', ]
    template_name = 'blog/create_blog.html'
    success_url = '/blog/list'
    login_url = '/login/'

    def form_valid(self, form):
        """
        overriding form validation method to set author
        to the instance before writing to database
        """
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super(CreateBlog, self).form_valid(form)


class BlogList(mixins.LoginRequiredMixin, ListView):
    """View for show all the blogs"""
    model = Post
    paginate_by = 5
    login_url = '/login/'
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        """Overriding this method to filter using query parameter if it exist"""
        q = self.request.GET.get('q')
        if q:
            qs = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
            return qs
        return super(BlogList, self).get_queryset()


class SearchView(ListAPIView):
    """
    APIView for Searching Blog
    """
    serializer_class = SearchResponseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        overriding this method for lookup using query parameter

        :return: filtered queryset(by search keyword)
        """
        q = self.request.query_params.get("q")
        # querying only title field
        return Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        ).distinct().values("title")


class MyBlogs(mixins.LoginRequiredMixin, ListView):
    """
    View for listing all blogs by authenticated user
    """
    model = Post
    template_name = "blog/my_blogs.html"
    login_url = '/login/'
    paginate_by = 3

    def get_queryset(self):
        return super(MyBlogs, self).get_queryset().filter(author=self.request.user)


class BlogUpdateView(mixins.LoginRequiredMixin, UpdateView):
    """View for updating only authenticated user's blog"""
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/edit_blog.html'
    success_url = '/my-blog/'

    def get_queryset(self):
        """Overriding this method to show only authenticated user blog"""
        return  super(BlogUpdateView, self).get_queryset().filter(author=self.request.user)


class DeleteBlog(mixins.LoginRequiredMixin, DeleteView):
    """View to delete blog posted by authenticated user"""
    model = Post
    success_url = '/my-blog/'

    def get_queryset(self):
        """Overriding this method to filter using authenticated user"""
        return super(DeleteBlog, self).get_queryset().filter(author=self.request.user)

