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
        recipient_list = [email, ]
        email_list = '' 
        for i in recipient_list:
            email_list = email_list + i
        message = message +' '+ name +' '+ email_list
        subject = 'feedback from khanzo'
        email_from = settings.EMAIL_HOST_USER
        email_to = ['khanzoofficial@gmail.com']       
        send_mail( subject, message, email_from, email_to )
        return render(request, 'contact.html')

def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')

def point(request):
    if request.method == 'GET':
        return render(request, 'point.html')

def insurance(request):
    if request.method == 'GET':
        return render(request, 'insurance.html')