from django.shortcuts import redirect, render
from .models import tabla
from .forms import tablaForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def escultura(request):
    return render(request, 'core/escultura.html')   

def tejido(request):
    return render(request, 'core/tejido.html')     

def orfebreria(request):
    return render(request, 'core/orfebreria.html') 

def pintura(request):
    return render(request, 'core/pintura.html')       

def agregar(request):
    return render(request, 'core/agregar.html')    

def registro(request):
    return render(request, 'core/registro.html') 
    
def admin(request):
    return render(request, 'core/admin.html')

def registrof(request):
    return render(request, 'core/registrof.html')    

def tablacrud(request):
    tablas = tabla.objects.all()
    context = {'tablas':tablas}
    return render(request, 'core/tablacrud.html', context)  

def agregarcrud(request):
    if request.method == "POST":
        form = tablaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tablacrud')
    else:
        form = tablaForm()        

    context = {}    
    return render(request, 'core/agregarcrud.html', context)