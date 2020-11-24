from django.shortcuts import render
# Create your views here.

def index(request):
    print("Hola estoy en index...")
    context={}
    return render (request,'logistica/index.html', context)

def buscar_para_seguir(request):
    print("Estamos en la vista buscar para seguir")
    if request.method =='POST':
        mi_codigo= request.POST['codigo']

        if mi_codigo !="":
            try:
                prod = producto()
                prod = producto.objects.get(codigo=mi_codigo)
                if prod is not None:
                    print ("producto = ", prod)
                    context={'prod':prod}
                    return render(request,'logistica/index.html',context)
                else:
                    return render(request,'logistica/error_202.html',{})
            except prod.DoesNotExist:
                return render(request,'logistica/error/error_202.html',{})
        else:
            return render(request,'logistica/error/error_201.html', {})
    else:
        return render(request, 'logistica/error/error_203.html',{})