from django.shortcuts import render

# Create your views here.
def blog(request):
    """Renders the blog main page"""
    return render(request, 'blog/blog_index.html')
