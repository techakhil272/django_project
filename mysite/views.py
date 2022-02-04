from django.shortcuts import render
from datetime import datetime
from mysite.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def press(request):
    return render(request,'press.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request,'contact.html')
