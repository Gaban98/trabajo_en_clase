from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ViewCategory, name='ViewCategory'),
    path('product/<int:idCategory>', views.ViewProductCategory, name='ViewProductCategory'),
]