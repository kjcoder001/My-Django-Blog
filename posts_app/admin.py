from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    ''' Used to add more features or modifications to the default admin interface of Django'''

    list_display=['title','updated','timestamp'] # attribute/property/field of ModelAdmin class which says what should be displayed on the admin
    # interface .The items passed in the list are basically the fields of the corresponding model(Post).

    list_display_links=['updated'] #Use list_display_links to control if and which fields in list_display should
    # be linked to the “change” page for an object.e.g here the 'updated' DateTimeField will now link to another page which will
    # show the updated content.

    list_filter=['updated','timestamp'] # gives a filter dialougue box on the admin page which can be used to filter the posts
    # according to some parameter.e.g here the posts will be filtered acc to their timestamp(last week,last year,last month etc)
    # and latest updates

    search_fields=['title','content'] # provides a search engine on the admin page to search the content in our db

    list_editable=['title']# provides an option to edit the name of a feild provided in the list i.e it is editable
    class Meta:
        model=Post


admin.site.register(Post,PostModelAdmin)
