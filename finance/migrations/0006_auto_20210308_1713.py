# Generated by Django 3.1.4 on 2021-03-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20210308_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmodel',
            name='chequeNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
