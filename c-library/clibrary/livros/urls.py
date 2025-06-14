from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_livro, name='criar_livro'),
    path('listar/', views.listar_livros, name='listar_livros'),
    path('livro/<int:id>/', views.buscar_livro, name='buscar_livro'),
    path('livro/<int:id>/atualizar/', views.atualizar_livro, name='atualizar_livro'),
    path('livro/<int:id>/deletar/', views.deletar_livro, name='deletar_livro'),
]
