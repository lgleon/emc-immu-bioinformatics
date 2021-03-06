# Generated by Django 2.2.7 on 2020-01-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0001_initial'),
        ('requestform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='job', to='requestform.Jobs'),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
    ]
