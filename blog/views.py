from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth import mixins

# from blog.forms import BlogCreateForm
from blog.models import Post


def home_page(request):
    """Function for home page"""
    if request.user.is_authenticated:
        return redirect('blog:list')
    else:
        return redirect('users:login')


class CreateBlog(mixins.LoginRequiredMixin, CreateView):
    """
    View for creating blog
    """
    model = Post
    fields = ['title', 'content',]
    template_name = 'blog/create_blog.html'
    success_url = '/blog/list'
    login_url = '/login/'

    def form_valid(self, form):
        """
        overriding form validation method to save author as requested user
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


# def search_view(request):
#     """Function for search blogs"""
#     if request.is_ajax():
#         query = request.GET.get("word", "")
#         print(query)
#         blog_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
#         print("***",blog_list)
#         return JsonResponse({"data": blog_list}, safe=False)
#     return JsonResponse({"error": "Bad Request"}, status=400)

