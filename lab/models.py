from django.db import models
from django.utils import timezone, dateformat
from priority.models import Clients


class Team(models.Model):
    """
    Create models to have the profile for each member of the lab team and to know whos is working and making
    the job status update
    """
    name = models.CharField('name of the team member', max_length=5)
    position = models.CharField('owrk position of the eam member', max_length=5)
    resume = models.TextField('few lines of resume', max_length=200)
    experience = models.TextField('experience in data analysis',  max_length=120)
    skills = models.CharField(max_length=5)
    email = models.EmailField()

    job_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    jobstatus_update = models.TextField(max_length=300)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.name, self.date, self.job_name, self.jobstatus_update)

