# Generated by Django 3.1.4 on 2021-04-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_auto_20210413_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='isapprove',
            field=models.BooleanField(default=False),
        ),
    ]
