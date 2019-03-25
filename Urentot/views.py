from django.shortcuts import render
from django.http import HttpResponse
from .models import End

def index(request):
    
    exit = End.date_now.value_to_string
    
    context = {
        'exit': exit
    }
    return render(request, 'detail.html', context)
