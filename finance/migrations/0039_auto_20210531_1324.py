# Generated by Django 3.2 on 2021-05-31 07:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0038_auto_20210521_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 13, 24, 57, 893326)),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.loanmodel'),
        ),
    ]
