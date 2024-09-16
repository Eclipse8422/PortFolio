from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
import os

def home(request):
    return render(request, 'casebook/home.html')
    
def about(request):
    return render(request, 'casebook/about.html')

def projects(request):
    projects_show = [
        {
            'title': 'PortFolio',
            'desc': 'This is a functional shopping app intended to be a clone of Amazon and some of its features. This is clone is mixed with my design style and features that I thought would make it look better. This was created with React and incorporates Firebase Cloud firestore, firebase authentication, and accepts payments through Stripe.'
        },
        {
            'title': 'Amazon clone',
            'desc': 'This is a functional shopping app intended to be a clone of Amazon and some of its features. This is clone is mixed with my design style and features that I      thought would make it look better. This was created with React and incorporates Firebase Cloud firestore, firebase authentication, and accepts payments through Stripe.'
        },
        {
            'title': 'Blog',
            'desc': 'This is a functional shopping app intended to be a clone of Amazon and some of its features. This is clone is mixed with my design style and features that I thought would make it look better. This was created with React and incorporates Firebase Cloud firestore,     firebase authentication, and accepts payments through Stripe.'
        },
    ]
    return render(request, 'casebook/projects.html', {"projects_show": projects_show})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()


        send_mail(
                subject=f"Message by Portfolio from {name}",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
                from_email=email,   
                recipient_list=[os.environ.get('EMAIL_ID')],  
                fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent successfully :)')

        return redirect('/contact')
    
    return render(request, 'casebook/contact.html')