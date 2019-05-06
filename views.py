from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.

from .models import Post
    
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def ret_to_index(self):
    return HttpResponseRedirect(reverse("blog:index"))
    
