#views.py
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Flan, ContactForm #importamos la class Flan con los flans de la ddbb y la class contacform con los formularios de contacto de usuarios
from .forms import ContactFormForm  # Importa el formulario
from .forms import ContactFormModelForm  # Importa el nuevo formulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout 
from django.contrib import messages

# Create your views here.

@login_required(login_url='/registro') #si el usuario no esta autenticado se redirige a la vista "registro"
def welcome(request):
    titulo_pag = "Bienvenido a OnlyFlans"
    flanes_privados = Flan.objects.filter(is_private=True)
    nombre_usuario = request.user.get_username()
    context = {
        "nombre_usuario": nombre_usuario,
        'flanes': flanes_privados,
        'titulo_pag': titulo_pag,
    }
    return render(request, "welcome.html", context)   

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('welcome')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    

@login_required    
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')  # Redirige a la página de inicio 


def about(request):
    titulo_pag = "Acerca de OnlyFlans"
    nombre_usuario = None
    
    if request.user.is_authenticated:
        nombre_usuario = request.user.get_username()
    context = {
        "titulo_pag": titulo_pag,
        "nombre_usuario": nombre_usuario,
    }
    return render(request, "about.html", context)    
    
    
    
def contacto(request):
    titulo_pag = "Formulario de Contacto"
    nombre_usuario = None
    
    if request.user.is_authenticated:
        nombre_usuario = request.user.get_username()
    
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario en la base de datos
            return HttpResponseRedirect('/contacto_exitoso/')
    else:
        form = ContactFormModelForm()
        
    context = {
        'form': form,
        'titulo_pag': titulo_pag,
        "nombre_usuario": nombre_usuario,
    }
    return render(request, 'contacto.html', context)




def contacto_exitoso(request):
    titulo_pag = "Contacto Exitoso"
    return render(request, "contacto_exitoso.html", {"titulo_pag": titulo_pag})


def index(request):
    titulo_pag = "Bienvenido a OnlyFlans"
    flanes_publicos = Flan.objects.filter(is_private=False)
    nombre_usuario = None
    
    if request.user.is_authenticated:
        nombre_usuario = request.user.get_username()
        
    context = {
        'flanes': flanes_publicos,
        'titulo_pag': titulo_pag, 
        "nombre_usuario": nombre_usuario,
    }
    return render(request,"index.html", context)



def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if username and email and password:  # Verifica que todos los campos estén presentes
            user = User.objects.create_user(username, email, password)
            user.save() #inserta o actualiza los datos
            return redirect("/accounts/login/")
        else:
            # Manejar el caso donde algún campo está vacío
            return render(request, 'registro.html', {'error_message': 'Todos los campos son obligatorios'})
    else:
        # Si no es una solicitud POST, simplemente renderiza el formulario vacío
        return render(request, 'registro.html', {})



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""""""


"""
def logout(request):
    auth_logout(request)
    return redirect('index') 
"""

""" """  



"""
def registro(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = User.objects.create_user(username, email, password)
        
        user.save() #inserta o actualiza 
    return redirect("/index")
"""


        

""" metodo del formulario formcontactform
def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            #form.save()  # Guarda los datos del formulario en la base de datos
            return HttpResponseRedirect('/contacto_exitoso/')
        
    else:
        form = ContactFormForm()
        
    return render(request, 'contacto.html', {'form': form})
"""