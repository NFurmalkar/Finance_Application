# Generated by Django 3.2 on 2021-05-06 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0028_alter_transactionmodel_transactionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 7, 0, 31, 36, 479821)),
        ),
    ]