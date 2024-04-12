from django.shortcuts import render

# Create your views here.
def me(request):
    return render(request, 'mysite/me.html')

def resume(request):
    return render(request, 'mysite/resume.html')

