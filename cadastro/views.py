from django.shortcuts import render , redirect
from cadastro.forms import ClienteForm, MarcaForm, ModeloForm

from cadastro.models import Marca, Modelo, Cliente
from django.contrib import messages

# Create your views here.


def index(request):
    return render (request, 'index.html')

def segundo(request):
    return render (request, 'pagina2.html')

def incluirMarca(request):
    if request.method == 'POST':
        form = MarcaForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')

    form = MarcaForm()
    return render (request, 'marcas/form_marca.html', {'form':form})

def listarMarcas(request):
    marcas = Marca.objects.order_by('nome')
    return render(request, 'marcas/lista.html', {'marcas':marcas})

def alterarMarca(request, id):
    marca = Marca.objects.get(id=id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
         form.save()
         return redirect('listar_marcas')
    form = MarcaForm(instance=marca)
    return render (request, 'marcas/form_marca.html', {'form':form})

def excluirMarca(request, id):
    marca = Marca.objects.get(id=id)
    try:
        marca.delete()
    except:
        messages.error (request, 'Não foi possível excluir devido a associação')
    return redirect('listar_marcas')

def listarCliente(request):
    cliente = Cliente.objects.order_by('nome')
    return render(request, 'cliente/lista.html', {'cliente':cliente})

   
def incluirCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
    form = ClienteForm()
    return render (request, 'cliente/form_cliente.html', {'form':form})
     
def alterarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':    
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
    form = ClienteForm(instance=cliente)
    return render(request, 'cliente/form_cliente.html', {'form':form})

def excluirCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    try:
        cliente.delete()
    except:
        pass
    return redirect('listar_cliente')
    
def listarModelo(request):
    modelos = Modelo.objects.order_by('nome')
    return render (request, 'modelo/lista.html', {'modelos':modelos})

def incluirModelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_modelo')
    form = ModeloForm()
    return render (request, 'modelo/form_modelo.html',{'form':form} )

def alterarModelo(request, id):
    m = Modelo.objects.get(id=id)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance = m)
        if form.is_valid():
            form.save()
            return redirect('listar_modelo')
    form = ModeloForm(instance=m)
    return render (request,'modelo/form_modelo.html', {'form':form})
    
   

def excluirModelo(request, id):
    modelo = Modelo.objects.get (id = id)
    try:
     modelo.delete()
    except:
      pass    
    return redirect('listar_modelo')
