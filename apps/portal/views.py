from django.shortcuts import render
from apps.portal.models import Mueble, Decoracion, Arte, Exhibicion, Interiorismo

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
    
    productos = Mueble.objects.all()

    return render(request,
                   "portal/furnitures.html",
                   {"productos":productos})

def art(request): 
    '''
    display art catalog
    '''
    productos = Arte.objects.all()
    
    return render(request,
                       "portal/art.html",
                       {"productos":productos})

def decoration(request): 
    '''
    display decoration items catalog
    '''
    productos = Decoracion.objects.all()
    
    return render(request,
                       "portal/decoration.html",
                       {"productos":productos})

def exhibitions(request): 
    '''
    display exhibitions registered 
    '''
    exhibiciones = Exhibicion.objects.order_by("-Fecha_exhibicion")

    return render(request,
                   "portal/exhibitions.html",
                   {"exhibiciones": exhibiciones})

def interior_design(request): 
    '''
    display interior design photos
    '''
    interiores = Interiorismo.objects.order_by("-Fecha_registro")

    return render(request, 
                  "portal/interior.html",
                  {"interiores" : interiores})


### TODO: error handling routes 