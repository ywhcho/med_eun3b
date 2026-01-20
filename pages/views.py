from django.shortcuts import render

# Create your views here.

def home(request):
    """홈 페이지"""
    return render(request, 'pages/home.html')


def about(request):
    """About Us 페이지"""
    return render(request, 'pages/about.html')

