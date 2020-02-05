import stripe
from django.db import models

from emcbioinfo import settings
from requestform.models import Jobs

# Create your models here.

stripe.api_key = settings.STRIPE_SECRET


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    """ Priority-level and it is related like that: 0==none, 1==Low, 2==Mid and
    3==High"""
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=False)
    job = models.ForeignKey(Jobs, related_name='job', on_delete=models.DO_NOTHING, blank=False)


    def __str__(self):
        return "{0}-{1}".format(self.job, self.order)
