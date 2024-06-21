from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
def index(request):

    if request.method == 'POST':
        username = request.POST.get('inputUser')
        password = request.POST.get('inputContrasena')
        if username == 'admin' and password == 'admin':
            return redirect('/home/')
        else:
            return render(request, 'index.html', {'success_message': "Dni no valido o contraseña no valido"})
    else:
        return render(request, 'index.html')
 
        



    


    

def home(request):
    return render(request, 'home.html')
