from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_livro, name='criar_livro'),
    path('listar/', views.listar_livros, name='listar_livros'),
    path('livro/<int:id>/', views.buscar_livro, name='buscar_livro'),
    
]
