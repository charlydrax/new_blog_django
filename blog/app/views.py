from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

#une class pour les articles en globale
class PostList(generic.ListView):
    queryset = Post.object.filter(status=1).order_by('created_on')
    template_name = 'index.html'
#une class pour avoir les détails du models
class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'