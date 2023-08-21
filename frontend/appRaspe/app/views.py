from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .forms import ProductForm
from decimal import Decimal

# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hoamunod")

def user_list(request):

    api_url = 'http://localhost:5000/products'  # Agrega 'http://' al principio de la URL

    response = requests.get(api_url)

    """if response.status_code == 200:
        users = response.json()
        return render(request, 'user_list.html', {'users': users})
    else:
        return render(request, 'error.html', {'error_message': 'Error al obtener los datos'})"""
    productos=[]
    for p in response.json():       
        productos.append(p)   
    return render(request,"lista.html",{'productos': productos})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'codigo_raspe': form.cleaned_data['codigo_raspe'],
                'codigo_lote': form.cleaned_data['codigo_lote'],
                'precio': float(form.cleaned_data['precio'])  # Convertir a float
            }
            api_url = 'http://localhost:5000/products'  # Cambia esto por la URL de tu API
            response = requests.post(api_url, json=data)

            if response.status_code == 201:
                return redirect('/lista')
            else:
                # Manejar el caso de error en la respuesta de la API
                error_message = 'Error al guardar el producto en la API'
                return render(request, 'create_product.html', {'form': form, 'error_message': error_message})
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def delete_raspe():
    print("Eliminar")