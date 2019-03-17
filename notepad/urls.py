from django.urls import path
from .views import create_view

app_name = 'notepad'

urlpatterns = [
    path('create/',create_view, name='create'),
]
