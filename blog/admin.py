from django.contrib import admin

from .models import Post


#class PostModelAdmin(admin.ModelAdmin):
  #list_display = ["title","updated","timestamp"]
  #list_display_links = ["updated"]
  #list_filter = ["updated","timestamp"]
  #

#admin.site.register(Post,PostModelAdmin)
class PostModelAdmin(admin.ModelAdmin):

   list_display = ["title", "updated", "timestamp"]
   list_display_links = ["title","updated"]
   list_filter = ["updated", "timestamp"]
   #date_hierarchy = 'updated'
   search_fields = ["title","content"]
   #list_editable = ["title"]

   class Meta:
     model=Post

admin.site.register(Post,PostModelAdmin)


