from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from . forms import PostForm
from django.contrib import messages
# Create your views here. Views are the logic of what our website does . How it handles the various requests coming to it , e.g GET POST etc.
# Basically views are python functions that accept a request and render or return a response.Which view will be called up for a particular
# request depends on the mapping of the urls. Each view is mapped to a unique url.
# The urlpatterns list determines the url and the mapped function for that url.
def posts_list(request):
    '''Lists all the posts present in the database'''

    posts_queryset=Post.objects.all()
    context={'title':'Lists all the posts',
             'queryset':posts_queryset}

    return render(request,'post_list.html',context)


def post_create(request):
    '''Creates a new Post'''

    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Post Created Succesfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:

        context={'form':form}
        return render(request,'post_form.html',context)

# for commit=false:-https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
#This save() method accepts an optional commit keyword argument, which accepts either True or False. If you call save() with commit=False,
#then it will return an object that hasn't yet been saved to the database.
#In this case, it's up to you to call save() on the resulting model instance. This is useful if you want to do custom processing on the
#object before saving it, or if you want to use one of the specialized model saving options. commit is True by default.




def post_detail(request,id):
    '''Gets the details of a particular post'''

    post=get_object_or_404(Post,id=id)# first parameter is the klass name to which the object belongs
    context={'post':post}

    return render(request,'post_detail.html',context)

def post_update(request,id=None):
    '''View to update an existing post'''

    instance=get_object_or_404(Post,id=id)
    # get_object_or_404() parameters :- A Model class, a Manager, or a QuerySet instance from which to get the object.

    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Post Updated Succesfully!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        context={
        'title':instance.title,
        'form':form,
        'instance':instance
        }
        return render(request,'post_form.html',context)

def post_delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Succesfully deleted")
    return redirect('posts:posts_list')# posts-namespace
