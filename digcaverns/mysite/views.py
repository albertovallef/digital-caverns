import os

from django.conf import settings
from django.contrib import messages
from django.db import ProgrammingError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt

from mysite.forms import ContactMessageForm 
from mysite.models import Contact, ContactMessage


def home(request):
    """Renders the home page"""
    return render(request, 'mysite/home.html')

def resume(request):
    """Renders the resume page"""
    return render(request, 'mysite/resume.html')

def contact_me(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            first_name: str = form.cleaned_data['first_name']
            last_name: str = form.cleaned_data['last_name']
            email: str = form.cleaned_data['email'] 
            content: str = form.cleaned_data['content']
            try:
                contact, created = Contact.objects.get_or_create(email=email)
                if not created:
                    if contact.first_name != first_name:
                        contact.first_name = first_name
                    if contact.last_name != last_name:
                        contact.last_name = last_name
                    contact.save()
                print(f"New user was created: {contact}")

                ContactMessage.objects.create(contact=contact, content=content)
                messages.success(request, "Your message was sent successfully!")
            except ProgrammingError as error:
                print(error)
                messages.error(request, "Ooops! There was an unexpected error... Please, consider contacting me with a different method.")
        else:
            messages.error(request, "There was an error in your request, please try again!")
    else:
        messages.error(request, "Incorrect request method. Use POST to send your information.")
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

