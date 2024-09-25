from django.contrib import admin
from bookstore_app.models import Author, Category, Book, Customer, Order, Payment

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Payment)
