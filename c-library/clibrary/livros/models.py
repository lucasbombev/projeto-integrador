from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo