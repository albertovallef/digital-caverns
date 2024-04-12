from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')

def resume(request):
    return render(request, 'mysite/resume.html')

def blog(request):
    return render(request, 'mysite/blog.html')
