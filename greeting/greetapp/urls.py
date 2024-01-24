from django.urls import path
from .views import get_greeting

urlpatterns = [
    path('', get_greeting, name='get_greeting'),
]
