from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, 'index.html')

def HomeView(request):
    return render(request, 'home.html')