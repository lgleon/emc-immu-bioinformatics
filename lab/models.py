from django.db import models
from django.utils import timezone


class Team(models.Model):
    """
    Create models to have the profile for each member of the lab (team)
    """
    name = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images')
    jobtitle = models.CharField(max_length=10, blank=True)
    resume = models.TextField(max_length=200)
    experience = models.TextField(max_length=120)
    skills = models.CharField(max_length=5)
    email = models.EmailField()

    def __str__(self):
        return self.name



class BlogStatus(models.Model):
    title = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    name = models.CharField('name of the team member working in the project',max_length=5)#ForeignKey(Team, on_delete=models.CASCADE)
    status = models.TextField(max_length=300)


    def __str__(self):
        return self.status