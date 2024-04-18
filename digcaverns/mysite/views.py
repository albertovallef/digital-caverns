from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import os


def home(request):
    """Renders the home page"""
    return render(request, 'mysite/home.html')

def resume(request):
    """Renders the resume page"""
    return render(request, 'mysite/resume.html')

@xframe_options_exempt
def display_resume(request):
    """Returns requested pdf resource"""
    # Change this to the path where your PDF files are stored
    filename = "Resume-15-08-2022.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    print(file_path)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="' + os.path.basename(file_path) + '"'
            return response
    else:
        return HttpResponse("File not found.", status=404)

def blog(request):
    """Renders the blog main page"""
    # NOTE: This will be moved to a different project
    return render(request, 'mysite/blog.html')
