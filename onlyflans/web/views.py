from django.shortcuts import render


# Create your views here.
#def index(request):
#    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def welcome(request):
    return render(request, "welcome.html", {})
    
    
def index(request):
    context = {
        "nombre": "leo",
        "apellido": "llaupe",
        "flanes": ["flan1","flan2","flan3"]
    }

    return render(request,"index.html",context)