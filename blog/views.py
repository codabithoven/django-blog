from django.shortcuts import render
from django.utils import timezone
from .models import Post 
# . = current directory, views and models are in the same directory
# then we import the name of the model

# Create your views here.
# a view is a place we put the "logic" of our app 
# it wil request infos from the model.py we've created
# and pass it to a template

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
