from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

# instanciamos el router
router = DefaultRouter()
# registramos las rutas
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet, basename='category')
# registramos las rutas autogeneradas
urlpatterns = [
    path('', include(router.urls)),
]

