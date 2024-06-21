# myapp/views.py
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
        inputDocumento = request.POST.get('inputDni')  # Assuming inputDni is actually for documento
        inputContrasena = request.POST.get('inputContrasena')
        print(inputContrasena,inputDocumento)
        
        try:
            alumno = Alumno.objects.get(documento=inputDocumento)
            print(alumno)
        except Alumno.DoesNotExist:
            error_message = "Usuario incorrecto o contraseña incorrecta"
            return render(request, 'login.html', {'error_message': error_message})
        if inputContrasena == alumno.contraseña:
            print("estoy aca")  # Comparing passwords securely
            request.session['alumno_id'] = alumno.idAlumno  # Store alumno_id in session for further use
            return redirect('home')  # Redirect to home view
        else:
            error_message = "Usuario incorrecto o contraseña incorrecta"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
@never_cache
def home(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
        try:
            alumno = Alumno.objects.get(pk=alumno_id)
            return render(request, 'home.html', {'alumno': alumno})
        except Alumno.DoesNotExist:
            # Si el alumno no existe, limpiar la sesión y redirigir a la página de inicio de sesión
            del request.session['alumno_id']
    
    return redirect('login')
@never_cache
def logout(request):
    del request.session['alumno_id']
    return redirect('login')
