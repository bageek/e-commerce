from django.contrib import admin
from .models import Category, Customer, Product, Order

# Enhanced admin for Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Enhanced admin for Customer  
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['first_name']

# Enhanced admin for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_sale', 'sale_price', 'in_stock', 'featured']
    list_filter = ['category', 'is_sale', 'in_stock', 'featured', 'brand', 'material']
    search_fields = ['name', 'description', 'brand']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'price', 'is_sale', 'sale_price')
        }),
        ('Images', {
            'fields': ('image', 'image_2', 'image_3', 'image_4')
        }),
        ('Jewelry Specific', {
            'fields': ('material', 'carat', 'gemstone'),
            'classes': ('collapse',)
        }),
        ('Makeup Specific', {
            'fields': ('brand', 'shade', 'skin_type'),
            'classes': ('collapse',)
        }),
        ('General Attributes', {
            'fields': ('color', 'size', 'weight', 'in_stock', 'featured')
        }),
        ('SEO', {
            'fields': ('meta_description', 'slug'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

# Enhanced admin for Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'date', 'status']
    list_filter = ['status', 'date']
    search_fields = ['product__name', 'customer__first_name', 'customer__last_name']
