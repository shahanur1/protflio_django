from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


# Home/Index View
def index(request):
    # check post method and request type
    if request.method == 'POST'and request.is_ajax():
        # check for empty name field
        if request.POST['name'] == "":
            username = "Shahanur Islam Shago"   #  set default name
        else:
            username = request.POST['name']
        # check for select field
        if request.POST['gender'] == "Select":
            gender = "f"
        else:
            gender = request.POST['gender']
        # return name and gender to success in ajax call top update content
        return HttpResponse(json.dumps({'name': username, 'gender': gender}))
    else:
        return render(request, 'mypf/home.html')


#Portfolio View
def portfolio(request):
    return render(request, 'mypf/portfolio.html')

#services View
def services(request):
    return render(request, 'mypf/services.html')

#blog View
def blog(request):
    return render(request, 'mypf/blog.html')


# Contact View
def contact(request):
    if request.method == 'POST':
        if request.method == 'POST':
		        message = request.POST['message']
		        send_mail('Contact Form',
		        message, 
		        settings.EMAIL_HOST_USER,
		        ['mdshahanurislamshagor@gmail.com'], 
	            fail_silently=False)
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
            # Saving Form data to Database
        form.save()
        messages.success(request, 'You Have a New Message')
        return render(request, 'mypf/contact.html')
    else:
        return render(request, 'mypf/contact.html')







