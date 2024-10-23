from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, from Django! ready with chai aur samosa")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, from Django! ready with chai aur samosa from about page")

def contact(request):
    return HttpResponse("Hello, from Django! ready with chai aur samosa from contact page")