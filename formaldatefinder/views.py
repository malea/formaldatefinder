from django.http import HttpResponse
from django.shortcuts import render
from os import getenv

def index(request):
    context = {
        'fb_app_id': getenv('FB_APP_ID')
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        data = ""
        for k,v in request.POST.items():
            data += k + " : " + v + "\n"
        return HttpResponse(data)
    return render(request, 'register.html')

def upcoming(request):
    return render(request, 'upcoming.html')


