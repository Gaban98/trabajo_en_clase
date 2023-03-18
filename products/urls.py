from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ViewCategory, name='ViewCategory'),
    path('products/<int:idCategory>', views.ViewProductCategory, name='ViewProductCategory'),
    path('product/<int:idProduct>', views.ViewProduct, name='ViewProduct'),
]