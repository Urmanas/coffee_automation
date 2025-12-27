from django.shortcuts import render

def index(request):
    return render(request, 'orders/index.html')

def contact(request):
    return render(request, 'orders/contact.html')