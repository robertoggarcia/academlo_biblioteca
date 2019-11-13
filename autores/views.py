from rest_framework import viewsets
from autores.models import Autor
from autores.serializers import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """
    Autor endpoint (ViewSet)
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
