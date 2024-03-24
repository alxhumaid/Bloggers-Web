from django.contrib import admin 
from blogger.models import post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'author', 'publish','status')
 
 

    
admin.site.register(post, PostAdmin)

# Register your models here.
