#views.py
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Flan, ContactForm #importamos la class Flan con los flans de la ddbb y la class contacform con los formularios de contacto de usuarios
from .forms import ContactFormForm  # Importa el formulario
from .forms import ContactFormModelForm  # Importa el nuevo formulario

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario en la base de datos
            return HttpResponseRedirect('/contacto_exitoso/')
        
    else:
        form = ContactFormModelForm()
        
    return render(request, 'contacto.html', {'form': form})

"""
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

def contacto_exitoso(request):
    return render(request, "contacto_exitoso.html", {})





def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos,
    }
    return render(request,"index.html",context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        "nombre": "leo",
        "apellido": "llaupe",
        'flanes': flanes_privados,
    }
    #request.session ['nombre'] = "leo"
    return render(request, "welcome.html", context)
    
    
def about(request):
    return render(request, "about.html", {})

def login(request):
    #get -> mostrar en html
    if request.method == "GET":
        return render(request, "login.html", {})
    
    #post -> capturar datos de html
    if request.method == "POST":
        print(request.post)


