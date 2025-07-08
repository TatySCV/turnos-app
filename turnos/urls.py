from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TurnoViewSet
from .views import ServicioViewSet, PeluqueraViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r'turnos', TurnoViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'profesionales', PeluqueraViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
