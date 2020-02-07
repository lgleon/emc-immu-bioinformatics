from django.db import models
from django.utils import timezone, dateformat


# Create your models here.


class Contact(models.Model):
    """
    Create models to have a record of the people who contact our lab and will possible users/clients
    """
    name = models.CharField('Name', max_length=30)
    email = models.EmailField()
    institution = models.CharField('University, company', max_length=30)
    inquiry = models.TextField('Question', max_length=200)


    def __str__(self):
        return "{0}-{1}-{2}".format(self.name, self.email, self.inquiry)