from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def resource(request):
    return render(request, 'resource.html')

def about_us(request):
    return render(request, 'about.html')
