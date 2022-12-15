from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
    path('update_computador/<int:id>', views.update_computador, name="update_computador"),
    path('excluir_computador/<int:id>', views.excluir_computador, name="excluir_computador"),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente"),

]
