from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Article

# Create your views here.
def blog(request):
    """Renders the blog main page"""
    return render(request, 'blog/index.html')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_template.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.increment_views()
        return obj






class ArticleListView(ListView):
    model = Article
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
     
