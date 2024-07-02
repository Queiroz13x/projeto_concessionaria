from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('/segundo', views.segundo, name='segundo'),

    #Marcas 
    path('/listar_marcas', views.listarMarcas, name = 'listar_marcas'),
    path('/incluir_marca', views.incluirMarca, name='incluir_marca' ),
    path('/alterar_marca/ <int:id>', views.alterarMarca, name='alterar_marca'), 
    path('/excluir_marca/ <int:id>', views.excluirMarca, name='excluir_marca'),  

    #Cliente 
    path('/listar_cliente', views.listarCliente, name = 'listar_cliente'),
    path('/incluir_cliente', views.incluirCliente, name='incluir_cliente' ),
    path('/alterar_ciente/ <int:id>', views.alterarCliente, name='alterar_cliente'), 
    path('/excluir_cliente/ <int:id>', views.excluirCliente , name='excluir_cliente'),

    #Modelos
    path ('/listar_modelo', views.listarModelo,name='listar_modelo'),
    path('/incluir_modelo', views.incluirModelo,name='incluir_modelo'),
    path('/alterar_modelo/<int:id>', views.alterarModelo,name = 'alterar_modelo'),
    path ('/excluir_modelo/<int:id>', views.excluirModelo, name = 'excluir_modelo'),
]