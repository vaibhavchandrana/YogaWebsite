# Generated by Django 4.1.4 on 2022-12-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='batch',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
