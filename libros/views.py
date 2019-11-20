from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from libros.serializers import LibroSerializer, CreateLibroSerializer
from libros.models import Libro


class LibroViewSet(viewsets.ModelViewSet):
    """
    Libro endpoint (viewset)
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer

    @action(detail=True, methods=['GET'])
    def autores(self, request, pk=None):
        # /libros/1/autores
        libro = self.get_object() # => Libro.objects.get(id=1)
        autores = libro.autores.all()
        # autores = Autor.objects.filter(libro__id=libro.id)
        serialized = AutorSerializer(autores, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def editorial(self, request, pk=None):
        libro = self.get_object()
        editorial = libro.editorial
        serialized = EditorialSerializer(editorial)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=False, methods=['GET'])
    def recent(self, request):
        # /libros/recent/
        # /libros/publicados/
        libros = Libro.objects.all().order_by('-fecha_publicacion')
        serialized = LibroSerializer(libros, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
