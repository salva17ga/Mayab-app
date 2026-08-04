from django.shortcuts import render
from .models import Producto

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
    furnitures = Producto.objects.filter(Categoria = 'Mueble').all()

    return render(request, "portal/furnitures.html", {furnitures:furnitures})

def art(request): 
    '''
    display art catalog
    '''
    return render(request, "portal/art.html")

def decoration(request): 
    '''
    display decoration items catalog
    '''
    return render(request, "portal/decoration.html")

def exhibitions(request): 
    '''
    display exhibitions registered 
    '''
    return render(request, "portal/exhibitions.html")

### TODO: error handling routes 