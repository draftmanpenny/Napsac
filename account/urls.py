from django.urls import path
from account.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from .api import RegisterApi


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterApi.as_view()), 
]
