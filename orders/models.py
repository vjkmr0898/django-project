from django.db import models
from datetime import datetime
from base.models import Products

# Create your models here.

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=45)
    date=models.DateTimeField(default=datetime.now)
    mobile_number= models.CharField(max_length=15)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2,null=True)

class OrderDetails(models.Model):
    order_id=models.ForeignKey(Orders, on_delete=models.CASCADE,null=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2)