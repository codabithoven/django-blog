from django.shortcuts import render

# Create your views here.
# a view is a place we put the "logic" of our app 
# it wil request infos from the model.py we've created
# and pass it to a template

def post_list(request):
    return render(request, 'blog/post_list.html', {})
    