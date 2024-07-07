from django.db import models
import datetime

# Create a model of categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "categories"

# Create a model of products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    description = models.CharField(max_length=2500, default='', blank= True, null = True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return f'{self.name}'

# Create a model of customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=9)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create a model of customers' orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    address = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    phone = models.CharField(max_length=9, default='', blank= True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product