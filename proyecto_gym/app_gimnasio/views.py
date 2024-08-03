from django.shortcuts import render, redirect
from .models import Usuario
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def index(request):
    return redirect('login')
@never_cache
def login(request):
    if 'Usuario_id' in request.session:
        del request.session['Usuario_id']
    if request.method == 'POST':
        inputDocumento = request.POST.get('inputDni')  
        inputContrasena = request.POST.get('inputContrasena')
        try:
            Usuariox = Usuario.objects.get(documento=inputDocumento)
            print(inputContrasena)
            print(Usuariox.contraseña)
        except Usuario.DoesNotExist:
            error_message = "Usuario incorrecto o contraseña incorrecta no existe usuario"
            return render(request, 'login.html', {'error_message': error_message})
        if inputContrasena == Usuariox.contraseña:
            #print("estoy aca") 
            request.session['Usuario_id'] = Usuariox.idUsuario  
            return redirect('home')
        else:
            error_message = "Usuario incorrecto o contraseña incorrecta nose que pasa"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
@never_cache
def home(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
        try:
            #Pagina de inicio Home
            Usuariox = Usuario.objects.get(pk=Usuario_id)
            tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
            if tipousuario == 'Administrador':
                return render(request, 'home.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
            elif tipousuario == 'Profesor':
                return render(request, 'home.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
            else:
                return render(request, 'home.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
            
        except Usuario.DoesNotExist:
            del request.session['Usuario_id']
    
    return redirect('login')

def agregarUsuario(request):
    Usuario_id = request.session.get('Usuario_id')
    Usuariox = Usuario.objects.get(pk=Usuario_id)
    tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
    print(Usuario, tipousuario)
    if tipousuario == 'Administrador':
        if request.method == 'POST':
            nombre = request.POST.get('inputName')
            apellido = request.POST.get('inputSurname')
            documento = request.POST.get('inputDni')
            contrasena = request.POST.get('inputContrasena')
            telefono = request.POST.get('inputTel')
            tipousuario = request.POST.get('inputRol')
            try:
                Usuario.objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    documento=documento,
                    contraseña=contrasena,
                    telefono=telefono,
                    tipousuario=tipousuario
                )
                return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'Usuario':Usuariox , 'success_message': 'Usuario agregado correctamente'})
            except ValidationError as e:
                error_message = e.message  # Mensaje de error general
                return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'Usuario':Usuariox ,'error_message': error_message})
        else:
            return render(request, 'agregarUsuario.html', {'tipousuario': tipousuario, 'Usuario':Usuariox})
    else:
        return redirect('home')

def  agregarClase(request):
    Usuario_id = request.session.get('Usuario_id')
    Usuario = Usuario.objects.get(pk=Usuario_id)
    tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
    if tipousuario == 'Administrador':
        return render(request, 'agregarClase.html', {'tipousuario': tipousuario, 'Usuario':Usuario})
    else:
        return redirect('home')

    

@never_cache
def logout(request):
    if 'Usuario_id' in request.session:
        del request.session['Usuario_id']
    return redirect('login')


def clases(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
            try:
                #Pagina de inicio Home
                Usuariox = Usuario.objects.get(pk=Usuario_id)
                tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'clases.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'clases.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
                else:
                    return render(request, 'clases.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
                
            except Usuario.DoesNotExist:
                del request.session['Usuario_id']
            
        
    return redirect('login')

def reservas(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
            try:
                #Pagina de inicio Home
                Usuariox = Usuario.objects.get(pk=Usuario_id)
                tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'reservas.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'reservas.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
                else:
                    return render(request, 'reservas.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
                
            except Usuario.DoesNotExist:
                del request.session['Usuario_id']
            
        
    return redirect('login')
            

def cuotas(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
            try:
                #Pagina de inicio Home
                Usuariox = Usuario.objects.get(pk=Usuario_id)
                tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
                else:
                    return render(request, 'cuotas.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
                
            except Usuario.DoesNotExist:
                del request.session['Usuario_id']
            
        
    return redirect('login')

def perfil(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
            try:
                #Pagina de inicio Home
                Usuariox = Usuario.objects.get(pk=Usuario_id)
                tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'perfil.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'perfil.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
                else:
                    return render(request, 'perfil.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
                
            except Usuario.DoesNotExist:
                del request.session['Usuario_id']
            
        
    return redirect('login')


def usuarios(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
        try:
            Usuariox = Usuario.objects.get(pk=Usuario_id)
            tipousuario = Usuariox.tipousuario

            query = request.GET.get('q')
            filtro_tipo = request.GET.get('tipo')
            
            if query:
                all_usuarios = Usuario.objects.filter(nombre__icontains=query)
            elif filtro_tipo:
                all_usuarios = Usuario.objects.filter(tipousuario=filtro_tipo)
            else:
                all_usuarios = Usuario.objects.all()

            paginator = Paginator(all_usuarios, 6)  # Mostrar 6 usuarios por página
            
            page_number = request.GET.get('page')
            Usuarioxs = paginator.get_page(page_number)
            
            if tipousuario == 'Usuario':
                return redirect('home')  # Usuario
            elif tipousuario == 'Administrador':    
                return render(request, 'usuarios.html', {
                    'tipousuario': tipousuario,
                    'Usuario': Usuariox,
                    'Usuarioxs': Usuarioxs,
                    'query': query,
                    'filtro_tipo': filtro_tipo
                })  # Administrador
                
        except Usuario.DoesNotExist:
            del request.session['Usuario_id']
            return redirect('login')  # O alguna otra página en caso de que el usuario no exista
    else:
        return redirect('login')

    

def notificaciones(request):
    Usuario_id = request.session.get('Usuario_id')
    if Usuario_id:
            try:
                #Pagina de inicio Home
                Usuariox = Usuario.objects.get(pk=Usuario_id)
                tipousuario = Usuario.objects.get(pk=Usuario_id).tipousuario
                if tipousuario == 'Administrador':
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario , 'Usuario':Usuariox}) #Usuario
                elif tipousuario == 'Profesor':
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})#Administrador
                else:
                    return render(request, 'notificacion.html', {'tipousuario': tipousuario  , 'Usuario':Usuariox})
                
            except Usuario.DoesNotExist:
                del request.session['Usuario_id']


@require_http_methods(["DELETE"])
def delete_usuario(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        usuario = get_object_or_404(Usuario, id=id)
        usuario.delete()
        return JsonResponse({'message': 'Usuario eliminado correctamente'}, status=200)
    else:
        return JsonResponse({'message': 'Solicitud no permitida'}, status=400)








