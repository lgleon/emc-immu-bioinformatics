from django.db import models
from priority.models import Clients
from users.models import User


class Jobs(models.Model):
    """
    Here we are going to create a model for any Job request, which include a first part for who is
    requesting teh job7analysis, second part some details about the data and a third part to create
    models for gadering more information regarding the type of analysis and research project

    """

    job_name = models.CharField('title for the request job', max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    is_priority = models.ForeignKey(Clients, on_delete=models.CASCADE)

    subject = models.CharField('short summary of the project subject', max_length=200)
    research_question = models.CharField(max_length=200)
    sample_number = models.IntegerField()
    expectations = models.CharField('what do you expect to get form this analysis', max_length=200)
    deadline = models.DateTimeField(blank=True)

    data_type = models.CharField('DNA, RNA, miRNAs, scRNA others', max_length=10)
    alignment = models.BooleanField(blank=False)
    annotation = models.BooleanField(blank=False)
    de_analysis = models.CharField(max_length=100)
    other_analysis = models.CharField(max_length=200)
    detailed_question = models.TextField(blank=False)
    detailed_summary = models.TextField(blank=False)
    other_info = models.TextField(blank=True)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.job_name, self.usuario, self.project, self.supervisor)
