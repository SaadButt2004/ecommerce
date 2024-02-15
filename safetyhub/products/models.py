from django.db import models
from base.models import BaseModel
from django.utils.text import slugify



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category_image = models.ImageField(upload_to="categories")


    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.category_name)
    #     super(Category , self).save(*args , **kwargs)

    def __str__(self):
        return self.category_name
            

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()


    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super(Product , self).save(*args , **kwargs)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    Product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image = models.ImageField(upload_to="product")