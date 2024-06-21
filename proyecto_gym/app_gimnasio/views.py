from django.shortcuts import render, redirect
from .models import Alumno
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect('login')
@never_cache
def login(request):
    if 'alumno_id' in request.session:
        del request.session['alumno_id']
    if request.method == 'POST':
        inputDocumento = request.POST.get('inputDni')  
        inputContrasena = request.POST.get('inputContrasena')
        try:
            alumno = Alumno.objects.get(documento=inputDocumento)
            print(alumno)
        except Alumno.DoesNotExist:
            error_message = "Usuario incorrecto o contraseña incorrecta"
            return render(request, 'login.html', {'error_message': error_message})
        if inputContrasena == alumno.contraseña:
            #print("estoy aca") 
            request.session['alumno_id'] = alumno.idAlumno  
            return redirect('home')
        else:
            error_message = "Usuario incorrecto o contraseña incorrecta"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
@never_cache
def home(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
        try:
            #Pagina de inicio Home
            alumno = Alumno.objects.get(pk=alumno_id)
            return render(request, 'home.html', {'alumno': alumno})
        except Alumno.DoesNotExist:
            del request.session['alumno_id']
    
    return redirect('login')
@never_cache
def logout(request):
    if 'alumno_id' in request.session:
        del request.session['alumno_id']
    return redirect('login')
