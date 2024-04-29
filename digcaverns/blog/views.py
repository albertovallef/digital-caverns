from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from markdown import markdown

from blog.models import Article

# Create your views here.
class ArticleDetailView(DetailView):
    """Rendering individual `Article` models"""

    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article_detail'

    def get_context_data(self, **kwargs):
        """Process article content before rendering page"""
        context = super().get_context_data(**kwargs)
        article = context["article_detail"]
        if article.content:
            article.html_content = markdown(article.content, 
                                            extensions=['fenced_code', 
                                                        'codehilite'],
                                            extension_configs={
                                            'codehilite': {
                                            'css_class': 'codehilite',
                                            'linenums': True
                                            }
                                            })
        return context
        

    def get_object(self, queryset=None):
        """Increase views everytime the article is clicked"""
        obj = super().get_object()
        obj.increment_views()
        return obj


class ArticleListView(ListView):
    """Rendering list of `Article` models"""

    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
     
