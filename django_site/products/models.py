from django.db import models
from djmoney.models.fields import MoneyField
class Product(models.Model): 
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name = 'products')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    image = models.ImageField(upload_to = '', default = 'pics/none.jpg', blank = True)

    def __str__(self):
        return self.title

class Category(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title

        