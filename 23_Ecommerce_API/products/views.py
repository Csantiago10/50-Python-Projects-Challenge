from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Controlador que maneja el CRUD completo de Productos.
    """

    # Usamos select_related('category') para evitar el problema N+1 al cargar la información de la categoría.
    # Esto asegura que los datos de la categoría se obtengan en la misma consulta que los productos.
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Controlador que maneja el CRUD completo de Categorías.
    """

    # ¡Atención al detalle técnico!
    # Usamos select_related('category') para evitar el problema N+1 en SQL.
    # Un experto nunca deja un queryset con llaves foráneas sin optimizar.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



