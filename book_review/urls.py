from .views import index, contact, about
from django.urls import path

urlpatterns = [
    path('', index),
    path('contact/',contact),
    path('about/',about)
]