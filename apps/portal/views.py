from django.shortcuts import render
from apps.portal.models import Mueble, Decoracion, Arte, Exhibicion, Interiorismo
from django.shortcuts import render, get_object_or_404

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
    categoria = request.GET.get("categoria")
    if categoria: 
        productos = Mueble.objects.filter(Categoria=categoria)
    else:
        productos = Mueble.objects.all()

    tipo_producto = 'Mueble'

    return render(request,
                   "portal/furnitures.html",
                   {"productos":productos,
                    "tipo_producto": tipo_producto,
                    "categorias": Mueble.CategoriasMuebles.choices,
                    "categoria_actual": categoria})

def art(request): 
    '''
    display art catalog
    '''
    categoria = request.GET.get("categoria")
    if categoria: 
        productos = Arte.objects.filter(Categoria=categoria)
    else:
        productos = Arte.objects.all()
    
    tipo_producto = 'Arte'
    
    return render(request,
                       "portal/art.html",
                       {"productos":productos,
                        "tipo_producto": tipo_producto,
                        "categorias": Arte.CategoriasArte.choices,
                        "categoria_actual": categoria})

def decoration(request): 
    '''
    display decoration items catalog
    '''
    categoria = request.GET.get("categoria")
    if categoria: 
        productos = Decoracion.objects.filter(Categoria=categoria)
    else:
        productos = Decoracion.objects.all()

    tipo_producto = 'Decoracion'
    
    return render(request,
                       "portal/decoration.html",
                       {"productos":productos,
                        "tipo_producto": tipo_producto,
                        "categorias": Decoracion.CategoriasDecoracion.choices,
                        "categoria_actual": categoria})

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

def product_detail(request, tipo, id): 
    '''
    display a template entirely dedicated to a product selected from a catalog
    '''
    if tipo == "Mueble":
        producto = get_object_or_404(Mueble, pk=id)

    elif tipo == "Arte":
        producto = get_object_or_404(Arte, pk=id)

    elif tipo == "Decoracion":
        producto = get_object_or_404(Decoracion, pk=id)

    return render(
        request,
        "portal/product_detail.html",
        {"producto": producto,
         "tipo_producto": tipo}
    )


### TODO: error handling routes 