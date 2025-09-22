from django.db import models
from django.utils import timezone
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)  # Increased for luxury items
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  
    description = models.CharField(max_length=500, default='', null=True, blank=True)   # Increased length
    image = models.ImageField(upload_to='uploads/products/')    
    
    # Additional images for gallery
    image_2 = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    
    # Jewelry specific fields
    material = models.CharField(max_length=100, null=True, blank=True)  # Gold, Silver, Platinum, etc.
    carat = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    gemstone = models.CharField(max_length=100, null=True, blank=True)
    
    # Makeup specific fields
    brand = models.CharField(max_length=100, null=True, blank=True)
    shade = models.CharField(max_length=50, null=True, blank=True)
    skin_type = models.CharField(max_length=50, null=True, blank=True)  # Dry, Oily, Combination, etc.
    
    # Common fields
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)  # For homepage featured products
    
    # Sale
    is_sale = models.BooleanField(default=False) 
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8) 
    
    # SEO and metadata
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/product/{self.id}'
    
    def get_sale_price(self):
        if self.is_sale and self.sale_price:
            return self.sale_price
        return self.price


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product