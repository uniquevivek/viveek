from django.shortcuts import render

def index(request):
    return render(request,'portfolio_v3.html')

def contact(request):
    return render(request, 'contact.html')

def certificates(request):
    return render(request, 'certificates.html')