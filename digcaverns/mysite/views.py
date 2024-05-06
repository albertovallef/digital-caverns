import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt


def home(request):
    """Renders the home page"""
    return render(request, 'mysite/home.html')

def resume(request):
    """Renders the resume page"""
    return render(request, 'mysite/resume.html')

def contact_me(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('fist')
        last_name = request.POST.get('last')
        content = request.POST.get('content')
        return redirect(home)

@xframe_options_exempt
def display_resume(request):
    """Returns requested pdf resource"""
    # TODO: Implement a system where I grab the most 
    # recent resume automatically; relates to issue#4 
    filename = "Resume-15-08-2022.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    print(file_path)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="Alberto_Valle_Resume.pdf"'
            return response
    else:
        return HttpResponse("File not found.", status=404)

