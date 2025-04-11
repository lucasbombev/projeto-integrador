from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
    
    class Leitor(models.Model):
        nome = models.CharField(max_length=255)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        cep = models.CharField(max_length=20)
        matricula = models.CharField(max_length=50, unique=True)

        def __str__(self):
            return self.nome