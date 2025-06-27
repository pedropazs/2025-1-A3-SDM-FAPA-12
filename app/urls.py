from django.urls import path
from . import views

urlpatterns = [
    path('itens/', views.listar_itens, name='listar_itens'),
    path('itens/<int:id>/', views.item_detail, name='item_detail'),
]
