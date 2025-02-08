from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """Для хранения категорий"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительская категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']

    def __str__(self):
        if self.parent:
            return f'{self.parent.name} > {self.name}'
        return self.name
    
    def save(self, *args, **kwargs):
            if not self.slug or self.slug.strip() == "":
                base_slug = slugify(f'{self.name}')
                unigue_slug = base_slug
                counter = 1
                while Category.objects.filter(slug=unigue_slug).exists():
                    unigue_slug = f'{base_slug}-{counter}'
                    counter += 1
                self.slug = unigue_slug
            super().save(*args, **kwargs)
            
            
            
class Product(models.Model):
    """Для хранения смартфонов"""
    name = models.CharField(max_length=100, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    year = models.IntegerField(verbose_name='Год производства')
    country = models.CharField(max_length=100, verbose_name='Страна производства')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
            if not self.slug or self.slug.strip() == "":
                base_slug = slugify(f'{self.name}')
                unigue_slug = base_slug
                counter = 1
                while Product.objects.filter(slug=unigue_slug).exists():
                    unigue_slug = f'{base_slug}-{counter}'
                    counter += 1
                self.slug = unigue_slug
            super().save(*args, **kwargs)



class Cart(models.Model):
    """Для хранения корзины"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма корзины')
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return f'{self.user.username} > {self.product.name}'
    
    def save(self, *args, **kwargs):
            if not self.slug or self.slug.strip() == "":
                base_slug = slugify(f'{self.user.username}-{self.product.name}')
                unigue_slug = base_slug
                counter = 1
                while Cart.objects.filter(slug=unigue_slug).exists():
                    unigue_slug = f'{base_slug}-{counter}'
                    counter += 1
                self.slug = unigue_slug
            self.total_price = self.quantity * self.product.price
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['-created_at']