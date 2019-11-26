from django.db import models
from autores.models import Autor
from editoriales.models import Editorial
from django.utils import timezone


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now())

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-fecha_publicacion',)
