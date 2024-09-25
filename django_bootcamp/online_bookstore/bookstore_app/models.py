from django.db import models

# Create your models here.

class Author(models.Model):

    """
    To store information about Author 
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):

    """
    To store information about Category
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):

    """
    To store information about Book
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
 
    def __str__(self):
        return self.title

class Customer(models.Model):
 
    """
    To store information about Customer
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):

    """
    To store information about Order
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} {self.book}"

class Payment(models.Model):

    """
    To store information about Payment
    """ 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order