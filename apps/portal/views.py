from django.shortcuts import render
from .models import Producto, Exhibicion

### views

def index(request): 
    '''
    main portal page 
    '''
    return render(request, "portal/index.html")

def about(request): 
    '''
    about us page ;  basic info about mayab
    '''
    return render(request, "portal/about.html")

def furnitures(request): 
    '''
    display furniture's catalog
    '''
    
    productos = Producto.objects.filter(Categoria = 'Mueble').all()

    return render(request,
                   "portal/furnitures.html",
                   {"productos":productos})

def art(request): 
    '''
    display art catalog
    '''
    productos = Producto.objects.filter(Categoria = 'Arte').all()
    
    return render(request,
                       "portal/art.html",
                       {"productos":productos})

def decoration(request): 
    '''
    display decoration items catalog
    '''
    productos = Producto.objects.filter(Categoria = 'Accesorio_decoracion').all()
    
    return render(request,
                       "portal/decoration.html",
                       {"productos":productos})

def exhibitions(request): 
    '''
    display exhibitions registered 
    '''
    exhibiciones = Exhibicion.objects.all()

    return render(request,
                   "portal/exhibitions.html",
                   {"exhibiciones": exhibiciones})

### TODO: error handling routes 