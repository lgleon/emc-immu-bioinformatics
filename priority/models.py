from django.db import models


class Clients(models.Model):
    """
    Create models to know which department and PI has the priority and for what ( I need to define types od priority )
    """
    department = models.CharField(max_length=5)
    project = models.TextField(max_length=200)
    priority_status = models.CharField(max_length=5)
    pi = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.department
