from django.urls import path

from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    # Use the primary key of the article for dynamic url reference
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
