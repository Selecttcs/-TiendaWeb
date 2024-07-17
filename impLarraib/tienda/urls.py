from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('escoger', views.escoger, name='escoger'), 
    path('adminBodega',views.adminBodega, name='adminBodega'),
    path('agregarProd', views.agregarProd, name='agregarProd'),
    path('editProd',views.editProd, name='editProd'),
    path('deleteProd/<str:pk>',views.deleteProd, name = "deleteProd"),
    path('encontrarProd/<str:pk>',views.encontrarProd, name = "encontrarProd"),

    path('adminExtranjeria', views.adminExtranjeria, name='adminExtranjeria'), 
    path('agregarOf',views.agregarOf,name='agregarOf'),
    path('deleteOf/<str:pk>',views.deleteOf, name= "deleteOf"),
    path('pago',views.pago, name='pago'),
    path('modificar',views.modificar, name='modificar')
]