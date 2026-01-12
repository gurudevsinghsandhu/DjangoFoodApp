from django.urls import path
from .api_views import SignupAPI, LoginAPI

urlpatterns = [
    path('api/signup/', SignupAPI.as_view()),
    path('api/login/', LoginAPI.as_view()),
]
