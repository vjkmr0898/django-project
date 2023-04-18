from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45)
    uom = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_items=models.IntegerField()
    to_sale= models.CharField(max_length=45,default='YES')