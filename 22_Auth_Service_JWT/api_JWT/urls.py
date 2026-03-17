
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

urlpatterns = [
    path('computers/', views.computer_list, name='computer_list'),
    path('computers/<int:pk>/', views.computer_detail, name='computer_detail'),
    # Endpoint para obtener el token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint para actualizar el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]