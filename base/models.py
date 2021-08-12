from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Seller(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.CharField(max_length=200, null= True, blank=True )
    rating = models.DecimalField(max_digits=10, decimal_places=2 ,null= True, blank=True)
    quantity = models.IntegerField(max_length=100, null= True, blank=True )
    max_to_sell = models.IntegerField(max_length=100, null= True, blank=True )
    min_to_sell = models.IntegerField(max_length=100, null= True, blank=True )
    unit_price = models.Double(max_length=200, null= True, blank=True )

class Transaction(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity_buyed = models.IntegerField(max_length=100, null= True, blank=True )
    paymentMethod = models.CharField(max_length=200, null= True, blank=True )
    total_price = models.Double(max_length=200, null= True, blank=True )
    tax_total = models.Double(max_length=200, null= True, blank=True )
    total = models.Double(max_length=200, null= True, blank=True )



