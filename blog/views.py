from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # queryset = Post.objects.all().order_by("created_on")
    # queryset = Post.objects.all()
    # model = Post
    template_name = "post_list.html"
