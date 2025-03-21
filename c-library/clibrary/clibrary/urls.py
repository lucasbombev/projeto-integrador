
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),
]
