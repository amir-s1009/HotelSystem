# Generated by Django 5.0.7 on 2024-07-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='duration',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]
