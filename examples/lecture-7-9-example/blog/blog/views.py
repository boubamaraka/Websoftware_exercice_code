from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from blog.models import BlogSite, BlogPost
from django.contrib.auth.models import User

def view_blog(request, author, blog_name):
  authorObj = User.objects.get(username=author)
  blog = BlogSite.objects.get(author=authorObj, name=blog_name)
  posts = BlogPost.objects.filter(blog=blog)
  template = get_template("blog.html")
  variables = Context(

  {'title' : blog_name,
  'author' : author,
  'posts' : posts })

  return HttpResponse( template.render(variables))
