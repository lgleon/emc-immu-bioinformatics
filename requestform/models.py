from django.db import models
from priority.models import Clients
from users.models import User


class Jobs(models.Model):
    """
    Here we are going to create a model for any Job request, which include a first part for who is
    requesting teh job7analysis, second part some details about the data and a third part to create
    models for gathering more information regarding the type of analysis and research project

    """
    HIGH = 'high'
    MID = 'mid'
    LOW = 'low'
    NONE = 'none'
    PRIORITY_CHOICES = [
        (HIGH, 'high'),
        (MID, 'mid'),
        (LOW, 'low'),
        (NONE, 'none'),
    ]

    job_name = models.CharField('title for this job', max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    priority_status = models.CharField(max_length=5, choices=PRIORITY_CHOICES, default=NONE)
    #contact_email = models.EmailField()

    subject = models.CharField('short summary of the project subject', max_length=200)
    research_question = models.CharField(max_length=200)
    sample_number = models.IntegerField()
    expectations = models.CharField('what you expect from the analysis', max_length=200)
    deadline = models.DateField(blank=True, null=True)

    data_type = models.CharField('DNA, RNA, miRNAs, scRNA others', max_length=10)
    alignment = models.BooleanField(blank=False)
    annotation = models.BooleanField(blank=False)
    de_analysis = models.CharField('Differential expression',max_length=100)
    other_analysis = models.CharField(max_length=200)
    detailed_question = models.TextField(blank=False)
    detailed_summary = models.TextField(blank=False)
    other_info = models.TextField(blank=True)

    is_payed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.job_name, self.usuario.email, self.subject, self.priority_status)

    def get_priority_value(self):
        if self.priority_status == Jobs.LOW:
            return 5
        elif self.priority_status == Jobs.MID:
            return 10
        elif self.priority_status == Jobs.HIGH:
            return 15
        else:
            return 0
