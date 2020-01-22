from django.db import models
from django.utils import timezone, dateformat


# Create your models here.


class Contact(models.Model):
    """
    Create models to have a record of the people who contact our lab and will possible users/clients
    """
    name = models.CharField('name of the person who contact', max_length=5)
    email = models.EmailField()
    institution = models.CharField('owrk position of the eam member', max_length=5)
    inquiry = models.TextField('few lines of resume', max_length=200)


    def __str__(self):
        return "{0}-{1}-{2}".format(self.name, self.email, self.inquiry)