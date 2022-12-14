from django.urls import path 
from .views import RegistrationApiView, UserBookShelfAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register', RegistrationApiView.as_view(), name="register"),
    path('login', TokenObtainPairView.as_view(), name="login" ),
    path('refresh-token', TokenRefreshView.as_view(), name="refresh-token" ),
    path('bookshelf', UserBookShelfAPI.as_view(), name='user-bookshelf')
]