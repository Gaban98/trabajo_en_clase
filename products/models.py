from django.db import models

# Create your models here.

class Category(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description_product = models.CharField(max_length=300, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=10, null=False)
    stock = models.IntegerField(null=True)
    imgBig = models.ImageField(upload_to='productos', null=True)
    imgSmall = models.ImageField(upload_to='iconos', null=True)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'