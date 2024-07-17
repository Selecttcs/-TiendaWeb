from django.shortcuts import render
from .models import Producto, Oferta
# Create your views here.

def index(request):
    context = {}
    return render(request,'tienda/index.html',context)

def login(request):
    context = {}
    return render(request,'tienda/login.html',context)

def escoger(request):
    context = {}
    return render(request, 'tienda/escoger.html',context)

def adminBodega(request):
    adminBodega = Producto.objects.all()
    context = {'inventario' : adminBodega}
    return render(request, 'tienda/adminBodega.html',context)

def agregarProd(request):
    inventario = Producto.objects.all()
    if request.method == 'POST':
        nombre=request.POST["nombre_prod"]
        sku=request.POST["sku"]
        precio=request.POST["precio"]
    obj = Producto.objects.create(

                                    name=nombre,
                                    sku=sku,
                                    precio=precio
                                )
    obj.save()
    context= {'mensaje': "Agregado con exito", 'inventario' : inventario}
    return render(request,'tienda/adminBodega.html',context)

def deleteProd(request, pk):
    context={}
    try:
        producto = Producto.objects.get(sku=pk)
        producto.delete()
        mensaje= "Datos eliminados"
        productos= Producto.objects.all()
        context={'inventario':productos, 'mensaje': mensaje}
        return render(request, 'tienda/adminBodega.html', context)
    except:
        mensaje= "Id no encontrado"
        productos= Producto.objects.all()
        context={'inventario':productos, 'mensaje': mensaje}
        return render(request, 'tienda/adminBodega.html', context)

def encontrarProd(request,pk):
    if pk != "":
        producto= Producto.objects.get(sku=pk)

        context={'producto':producto}
        if producto:
            return render(request, 'tienda/modificar.html', context)
        else:
            context={'mensaje':"Error, rut no existe"}
            return render(request, 'tienda/modificar.html', context)
        
def editProd(request):
    if request.method == "POST":
    
        nombre=request.POST["nombre"]
        sku=request.POST["sku"]
        precio=request.POST["precio"]

        prod = Producto()

        
        prod.name=nombre
        prod.sku=sku
        prod.precio=precio
        prod.save()

        context={'mensaje': "Datos actualizados correctamente", 'producto':prod}
        return render(request, 'tienda/modificar.html', context)
    else:
        #not post
        prod = Producto.objects.all()
        context={'producto':prod, 'mensaje' : "Error en actualizar"}
        return render(request, 'tienda/adminBodega.html', context)
########################################################################33
def adminExtranjeria(request):
    adminExtranjeria = Oferta.objects.all()
    context = {'ofertas' : adminExtranjeria}
    return render(request, 'tienda/adminExtranjeria.html',context)

def agregarOf(request):
    ofertas = Oferta.objects.all()
    if request.method == 'POST':
        id_oferta=request.POST["id"]
        nombre=request.POST["nombre_of"]
        contacto=request.POST["contacto"]
        cantidad=request.POST["cantidad"]
        costo=request.POST["costo"]
    obj = Oferta.objects.create(
                                    id_oferta=id_oferta,
                                    nombre=nombre,
                                    contacto=contacto,
                                    cantidad=cantidad,
                                    costo=costo
                                )
    obj.save()
    context= {'mensaje': "Agregado con exito", 'ofertas' : ofertas}
    return render(request,'tienda/adminBodega.html',context)

def deleteOf(request, pk):
    context={}
    try:
        oferta = Oferta.objects.get(id_oferta=pk)
        oferta.delete()
        mensaje= "Datos eliminados"
        ofertas = Oferta.objects.all()
        context={'ofertas':ofertas, 'mensaje': mensaje}
        return render(request, 'tienda/adminExtranjeria.html', context)
    except:
        mensaje= "Id no encontrado"
        ofertas= Producto.objects.all()
        context={'ofertas':ofertas, 'mensaje': mensaje}
        return render(request, 'tienda/adminExtranjeria.html', context)

def pago(request):
    context = {}
    return render(request, 'tienda/pago.html',context)

def modificar(request):
    context = {}
    return render(request,'tienda/modificar.html',context)