# Generated by Django 3.2.7 on 2021-09-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticker',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
