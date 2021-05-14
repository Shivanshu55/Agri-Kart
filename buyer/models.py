from django.db import models
from seller.models import Product
from AgriKart.models import UserProfile

# Create your models here.
class Cart(models.Model):

	class Meta():
		unique_together = ('user', 'product')

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
