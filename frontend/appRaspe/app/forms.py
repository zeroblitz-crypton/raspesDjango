from django import forms

class ProductForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    codigo_raspe = forms.CharField(label='Código Raspe', max_length=50)
    codigo_lote = forms.CharField(label='Código Lote', max_length=50)
    precio = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)