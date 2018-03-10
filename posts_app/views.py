from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here. Views are the logic of what our website does . How it handles the various requests coming to it , e.g GET POST etc.
# Basically views are python functions that accept a request and render or return a response.Which view will be called up for a particular
# request depends on the mapping of the urls. Each view is mapped to a unique url.
# The urlpatterns list determines the url and the mapped function for that url.
def posts_list(request):
    '''Lists all the posts present in the database'''

    posts_queryset=Post.objects.all()
    context={'title':'Lists all the posts',
             'queryset':posts_queryset}

    return render(request,'index.html',context)


def post_create(request):
    '''Creates a new Post'''
    return HttpResponse('<h1>Create</h1>')

def post_detail(request,id):
    '''Gets the details of a particular post'''

    post=get_object_or_404(Post,id=id)# first parameter is the klass name to which the object belongs 
    context={'post':post}

    return render(request,'post_detail.html',context)

def post_update(request):
    return HttpResponse('<h1>Update</h1>')

def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')
