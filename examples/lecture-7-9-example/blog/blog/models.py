from django.db import models
from django.contrib.auth.models import User

class BlogSite(models.Model):
    name = models.CharField(max_length=30)
    pretty_url = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.name + " by " + self.author.username


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text_body = models.TextField()
    blog = models.ForeignKey(BlogSite)
    in_reply_to = models.ForeignKey('self', blank=True, null=True)

    def has_replies(self):
        replies = BlogPost.objects.filter(in_reply_to=self)
        return len(replies) > 0

    def __str__(self):
        return self.blog.name + " : " + self.title
