# Импортируется родительский класс моделей            
from django.db import models 
from django.urls import reverse
# импорт из settings.AUTH_USER_MODEL
from shop_project import settings
from django.contrib.auth.models import User

# Создаем базовую модель нашего продукта
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True,related_name="products") 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('product_detail', args=[str(self.id)])

class Category(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title
    
class Order(models.Model): 
    product = models.ForeignKey(Product, on_delete='CASCADE') 
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE', null=True)
    #email = models.ForeignKey(email, on_delete='CASCADE', null=True)