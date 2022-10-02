from django.shortcuts import render
import sys


# Create your views here.

def home(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        data = {
            'name': file.name,
            'extention': file.name.split('.')[-1],
            'size': round(file.size / 1024 / 1024, 2),
            'mimo': file.content_type,
        }
        return render(request, 'Service/file.html', {'file': data})
    return render(request, 'Service/home.html', )
