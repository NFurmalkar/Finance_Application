# Generated by Django 3.2 on 2021-05-09 17:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0030_auto_20210507_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetailmodel',
            name='profileId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.signupmodel'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='profileId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.signupmodel'),
        ),
        migrations.AddField(
            model_name='partnermodel',
            name='profileId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.signupmodel'),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 22, 50, 43, 214156)),
        ),
    ]
