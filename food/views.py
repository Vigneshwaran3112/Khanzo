from django.shortcuts import render
from django.conf import settings 
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def store(request):
    if request.method == 'GET':
        return render(request, 'store.html')

def services(request):
    if request.method == 'GET':
        return render(request, 'services.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'feedback from khanzo'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list )
        return render(request, 'contact.html')

def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')