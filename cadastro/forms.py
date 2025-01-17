from django.forms import ModelForm  
from .models import Marca, Modelo
from .models import Cliente

class MarcaForm(ModelForm):
    class Meta: 
        model = Marca 
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ModeloForm(ModelForm):
    class Meta: 
        model = Modelo 
        fields = '__all__'