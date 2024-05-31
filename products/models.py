from django.db import models
from auth_user.models import User

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size, related_name='sizes')
    color = models.ManyToManyField(Color, related_name='colors')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.name
    

class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField()


    def __str__(self) -> str:
        return self.product.name
    

class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product_img/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.product.name
    


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.FileField(upload_to='product_video/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.product.name
    

class Order(models.Model):
    Cities = (
        ('Tashkent', 'Tashkent'),
        ('Buxara', 'Buxara'),
        ('Samarkand', 'Samarkand')
    )
    custumer = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.CharField(max_length=250, choices=Cities, default='Tashkent')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.product.name


class CashbackHistory(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.owner.username