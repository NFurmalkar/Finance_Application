# Generated by Django 3.2 on 2021-05-14 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0035_auto_20210514_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 23, 30, 3, 917479)),
        ),
    ]
