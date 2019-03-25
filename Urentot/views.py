from django.shortcuts import render
from django.http import HttpResponse
from .models import End
from datetime import datetime

def index(request):
    
    now = End.date_now
    exit = End.date_exit
    
    context = {
        'now' : now,
        'exit': exit
    }
    return render(request, 'detail.html', context)
