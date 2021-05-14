from django.db import models
from AgriKart.models import UserProfile

# Create your models here.
class Category(models.Model):
	catname = models.CharField(max_length=30, unique=True)

class Product(models.Model):
	pname = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	qty = models.IntegerField()
	desc = models.CharField(max_length=100)
	pic = models.ImageField(upload_to='product_image', blank=True)
	dated = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
