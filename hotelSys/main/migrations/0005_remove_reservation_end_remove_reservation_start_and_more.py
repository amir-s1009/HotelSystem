# Generated by Django 5.0.7 on 2024-07-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_reservation_duration_reservation_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start',
        ),
        migrations.AddField(
            model_name='reservation',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='endTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='startDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='startTime',
            field=models.TimeField(null=True),
        ),
    ]
