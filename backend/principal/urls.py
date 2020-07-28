from django.urls import include, path
from rest_framework.routers import DefaultRouter

from principal.views import UserViewGet, LoginView, LogoutView, MenuViewSet, MenuPeliculaViewSet, PeliculaViewSet, ImagenMuestraViewSet

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'peliculas', MenuPeliculaViewSet, basename='peliculas')
router.register(r'pelicula', PeliculaViewSet, basename='pelicula')
router.register(r'imagen_muestra', ImagenMuestraViewSet, basename='imagen_muestra')
urlpatterns = [
    path('', include(router.urls))
]
