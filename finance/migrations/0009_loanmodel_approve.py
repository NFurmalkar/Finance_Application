# Generated by Django 3.1.4 on 2021-03-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20210308_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='approve',
            field=models.BooleanField(default=True),
        ),
    ]
