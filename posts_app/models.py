# superuser :kushal,password : pass1234
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    updated=models.DateField(auto_now=True,auto_now_add=False)     # datetime fields don't show up in the models of
                                                                   # admin site,as they are going to get overwritten.
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
# auto_now =True indicates that the field(database) will be updated everytime a change is made whereas auto_now_add records only
# the initial entry of the post.

    def __str__(self): # this is what we see in the models table . If we dont write this the table says 'post object'
        '''Returns a name for each instance or object inn the db as the title of our post'''
        return self.title

    def get_absolute_url(self):
        '''Returns the absolute url for templates'''
        # returns the detail of that post :- /posts/1{id}
        return reverse("posts:post_detail", kwargs={"id":self.id}) #posts:post_detail-->posts is the namespace
        #return 'posts/{}'.format(self.id)
