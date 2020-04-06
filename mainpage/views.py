from django.shortcuts import render
from .models import Quotes

import random
# Create your views here


def mainpage(request):
    q = random.choice(Quotes.objects.all())
    return render(request,'mainpage.html',{'Quote':q})

def contact(request):
    return render(request,'contact.html')
