from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def login(request):
    return render(request, 'pages/login.html')

def story(request):
    return render(request, 'pages/story_info.html')

def search(request):
    return render(request, 'pages/search.html')