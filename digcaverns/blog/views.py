from django.http import Http404
from django.db.models import Q
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


    def get_object(self, queryset=None):
        """Increase views everytime the article is 
        clicked and filter content"""

        obj = super().get_object(queryset=queryset)
        today = timezone.now().date()

        if self.request.user.is_staff:  # Show everything to admin
            return obj  # Don't count admin views
        elif((obj.status=='RDY' and obj.publish_date <= today) or obj.status=='PUB'):
            obj.increment_views()
            return obj
        else:
            raise Http404("Article is not accessible at the moment")

    def get_context_data(self, **kwargs):
        """Process article content before rendering page"""
        context = super().get_context_data(**kwargs)
        article = context["article_detail"]
        if article.content:
            article.html_content = markdown(
                article.content, 
                extensions=['fenced_code', 'codehilite'],
                extension_configs={
                    'codehilite': { 
                        'css_class': 'codehilite',
                        'linenums': True}
                })
        return context


class ArticleListView(ListView):
    """Rendering list of `Article` models"""

    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles_list'
    paginate_by = 10

    def get_queryset(self):
        """Filter data based on user permissions and `Article` status"""
        today = timezone.now().date()
        if self.request.user.is_staff:
            # If admin access show all 
            return Article.objects.all()
        else:
            # Show only ready on publish date and published
            return Article.objects.filter(
                (Q(status='RDY') & Q(publish_date__lte=today)) | 
                    Q(status='PUB'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
     
