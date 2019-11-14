from rest_framework import viewsets
from libros.serializers import LibroSerializer, CreateLibroSerializer
from libros.models import Libro


class LibroViewSet(viewsets.ModelViewSet):
    """
    Libro endpoint (viewset)
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer

