from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)
    class Meta:
         verbose_name_plural='Categories'
    
    def get_absolute_url(self):
        return reverse('store : Category_list',args=[self.slug])
    
    def _str_(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    create_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='producty_create')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    in_stoke=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    class Meta:
         verbose_name_plural= 'Product'
         ordering= ['-created']

         def __str__(self):
             return self.title
         

