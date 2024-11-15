from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining a new token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing the token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),     # For verifying the token
    path('api/register/', views.register, name='register'),
    path('api/users/', views.all_users, name='users'),
]
