from django.shortcuts import render
from .models import *


# Create your views here.

def ViewCategory(request):
    ListCategory = Category.objects.all()
    context = {'caterias': ListCategory, 'titulo': 'Categorias de los productos }'}
    return render(request, 'products/category.html', context)

def ViewProductCategory(request, idCategory):
    NameCategory = Category.objects.get(id=idCategory)
    ListProduct = Product.objects.filter(category_product=idCategory)
    context = {'productos': ListProduct, 'titulo': 'Productos de la categoria: ' + NameCategory.description}
    return render(request, 'products/product.html', context)
