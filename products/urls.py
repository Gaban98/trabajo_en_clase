from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ViewCategory, name='ViewCategory'),

    path('products/<int:idCategory>', views.ViewProductCategory, name='ViewProductCategory'),
    path('product/<int:idProduct>', views.ViewProduct, name='ViewProduct'),
    
    path('AddShoppingCar/<int:idProduct>', views.AddShoppingCar, name='AddShoppingCar'),
    path('ShoppingCarView/', views.ShoppingCarView, name='ShoppingCarView'),
    path('DeleteProductCar/<int:idProduct>', views.DeleteProductCar, name='DeleteProductCar'),
    path('ChangeProductCar/', views.ChangeProductCar, name='ChangeProductCar'),

    path('pay/', views.Pay, name='Pay'),

]