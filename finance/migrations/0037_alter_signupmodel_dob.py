# Generated by Django 3.2 on 2021-05-14 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0036_alter_signupmodel_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 23, 40, 1, 520563)),
        ),
    ]
