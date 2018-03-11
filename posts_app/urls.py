from django.conf.urls import url
from django.contrib import admin
from posts_app import views

urlpatterns=[
url(r'^$',views.posts_list,name='posts_list'),
url(r'^create/$',views.post_create,name='post_create'),
url(r'^(?P<id>\d+)/$',views.post_detail,name='post_detail'),
url(r'^(?P<id>\d+)/edit/$',views.post_update,name='post_update'),
url(r'^(?P<id>\d+)/delete/$',views.post_delete,name='post_delete'),

]

# Link to django docs for urldispatcher :- https://docs.djangoproject.com/en/1.11/topics/http/urls/
# (?P<id>\d+) is called as a named-group and is used to get or retrieve info from the the url.Anythin between the the parantheses () is used
# get info from the url.This info is passed to the mapped view  as an additional parameter (apart from request). e.g the view function now
# is def post_detail(request,id):!
