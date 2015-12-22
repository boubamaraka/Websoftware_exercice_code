from blog.views import *
from blog.models import *
from django.contrib import admin

# This is where you collect models that should be accessible in Django admin interface

admin.site.register(BlogSite)
admin.site.register(BlogPost)
