from django.db import models
import django.utils
import datetime

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    last_transaction = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    from_cust = models.CharField(max_length=50)
    to_cust = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(default=django.utils.timezone.now)
    amount = models.IntegerField(default=0)
