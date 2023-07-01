from django.urls import path
from .views import SendRequest

urlpatterns = [
    path('', SendRequest)
]