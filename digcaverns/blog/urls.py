from django.urls import path

from blog.views import ArticleListView, blog 

urlpatterns = [
    #path('blog', ArticleListView.as_view(), name='articles-list'),
    path('blog', blog, name='blog'),
]
