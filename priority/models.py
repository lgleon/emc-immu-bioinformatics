from django.db import models
from users.models import User


class Clients(models.Model):
    """
    Create models for the user to register and became a client
    for that a supervisor can pay for the analysis (one or several) and for proprity (high, mid, low, none)
    Always wiil be a supervisor (which can have several users/students) and department

    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    department = models.CharField('PI Department',max_length=30)
    supervisor = models.CharField('Project PI', max_length=20)
    project = models.CharField('Project name', max_length=100)


    def __str__(self):
        return "{0}-{1}".format(self.supervisor, self.department)