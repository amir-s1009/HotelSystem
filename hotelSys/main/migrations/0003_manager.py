# Generated by Django 5.0.2 on 2024-03-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customer_password_customer_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('family', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
