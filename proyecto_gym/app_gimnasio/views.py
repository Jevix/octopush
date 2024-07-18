from django.shortcuts import render, redirect
from .models import Alumno
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


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
            tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
            if tipousuario == 'Administrador':
                return render(request, 'home.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
            elif tipousuario == 'Profesor':
                return render(request, 'home.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
            else:
                return render(request, 'home.html', {'tipousuario': tipousuario  , 'alumno':alumno})
            
        except Alumno.DoesNotExist:
            del request.session['alumno_id']
    
    return redirect('login')

def agregarUsuario(request):
    alumno_id = request.session.get('alumno_id')
    alumno = Alumno.objects.get(pk=alumno_id)
    tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
    print(alumno, tipousuario)
    if tipousuario == 'Administrador':
        if request.method == 'POST':
            nombre = request.POST.get('inputName')
            apellido = request.POST.get('inputSurname')
            documento = request.POST.get('inputDni')
            contrasena = request.POST.get('inputContrasena')
            telefono = request.POST.get('inputTel')
            tipousuario = request.POST.get('inputRol')
            try:
                Alumno.objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    documento=documento,
                    contraseña=contrasena,
                    telefono=telefono,
                    tipousuario=tipousuario
                )
                return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'alumno':alumno , 'success_message': 'Usuario agregado correctamente'})
            except ValidationError as e:
                error_message = e.message  # Mensaje de error general
                return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'alumno':alumno ,'error_message': error_message})
        else:
            return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'alumno':alumno})
    else:
        return redirect('home')

def  agregarClase(request):
    alumno_id = request.session.get('alumno_id')
    alumno = Alumno.objects.get(pk=alumno_id)
    tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
    if tipousuario == 'Administrador':
        return render(request, 'agregarClase.html', {'tipousuario': tipousuario, 'alumno':alumno})
    else:
        return redirect('home')

    

@never_cache
def logout(request):
    if 'alumno_id' in request.session:
        del request.session['alumno_id']
    return redirect('login')


def clases(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'clases.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'clases.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                else:
                    return render(request, 'clases.html', {'tipousuario': tipousuario  , 'alumno':alumno})
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']
            
        
    return redirect('login')

def reservas(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'reservas.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'reservas.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                else:
                    return render(request, 'reservas.html', {'tipousuario': tipousuario  , 'alumno':alumno})
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']
            
        
    return redirect('login')
            

def cuotas(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                else:
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario  , 'alumno':alumno})
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']
            
        
    return redirect('login')

def perfil(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'perfil.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'perfil.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                else:
                    return render(request, 'perfil.html', {'tipousuario': tipousuario  , 'alumno':alumno})
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']
            
        
    return redirect('login')


def usuarios(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Usuario':
                    return redirect('home') #Usuario
                elif tipousuario == 'Administrador':    
                    return render(request, 'usuarios.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                    
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']

    

def notificaciones(request):
    alumno_id = request.session.get('alumno_id')
    if alumno_id:
            try:
                #Pagina de inicio Home
                alumno = Alumno.objects.get(pk=alumno_id)
                tipousuario = Alumno.objects.get(pk=alumno_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario , 'alumno':alumno}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario  , 'alumno':alumno})#Administrador
                else:
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario  , 'alumno':alumno})
                
            except Alumno.DoesNotExist:
                del request.session['alumno_id']








