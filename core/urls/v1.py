from rest_framework import routers
from autores.views import AutorViewSet
from editoriales.views import EditorialViewSet
from libros.views import LibroViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', LibroViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
