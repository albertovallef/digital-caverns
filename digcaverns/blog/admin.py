from django.contrib import admin

from blog.models import Article, User

# Register your models here.
admin.site.register(Article)
admin.site.register(User)
