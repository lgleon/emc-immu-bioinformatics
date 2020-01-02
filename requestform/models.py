from django.db import models


class Jobs(models.Model):
    """
    Create models fro the request of bioinformatics jobs

    """
    title = models.CharField(max_length=10)
    data_type = models.CharField(max_length=10)
    #dpto = models.ForeignKey(Clients, on_delete=models.CASCADE)
    department = models.CharField(max_length=5) # Link to priority Clients
    status = models.CharField(max_length=10)
    is_priority = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class GeneralQuestions(models.Model):
    """
    Create models for the Biological part, to have more information regarding the project and data type
    """
    title = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    supervisor = models.CharField('name of the PI', max_length=10)
    requestee = models.CharField('name of Team member', max_length=5)
    subject = models.CharField('short summary of the project subject', max_length=200)
    research_question = models.CharField(max_length=200)
    authorship = models.CharField(max_length=3)
    sample_number = models.IntegerField()
    expectations = models.CharField('what do you expect to get form this analysis', max_length=200)
    deadline = models.DateTimeField()


    def __str__(self):
        return self.research_question


class AnalysisType(models.Model):
    """
    Create models for deeper information regarding the type of analysis and research project
    """
    title = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    datatype = models.CharField('DNA, RNA, miRNAs, scRNA others', max_length=10)
    alignment = models.BooleanField(blank=False)
    annotation = models.BooleanField(blank=False)
    de_analysis = models.CharField(max_length=100)
    other_analysis = models.CharField(max_length=200)
    detailed_question = models.TextField(blank=False)
    detailed_summary = models.TextField(blank=False)
    other_info = models.TextField(blank=True)


    def __str__(self):
        return self.detailed_question

