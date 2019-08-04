from django.shortcuts import render
from .models import Guide

def guide(request):
    all_guides = Guide.objects.all()
    return render(request, 'guide.html', {'guides': all_guides})
