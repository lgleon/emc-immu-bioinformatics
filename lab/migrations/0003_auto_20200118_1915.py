# Generated by Django 2.2.7 on 2020-01-18 18:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_team_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='team',
            name='experience',
            field=models.TextField(max_length=120, verbose_name='experience in data analysis'),
        ),
        migrations.AlterField(
            model_name='team',
            name='job_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priority.Clients'),
        ),
        migrations.AlterField(
            model_name='team',
            name='jobstatus_update',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=5, verbose_name='name of the team member'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(max_length=5, verbose_name='owrk position of the eam member'),
        ),
        migrations.AlterField(
            model_name='team',
            name='resume',
            field=models.TextField(max_length=200, verbose_name='few lines of resume'),
        ),
    ]