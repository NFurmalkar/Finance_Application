# Generated by Django 3.1.4 on 2021-04-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_auto_20210414_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactionModel',
            fields=[
                ('transactionID', models.AutoField(primary_key=True, serialize=False)),
                ('customerId', models.IntegerField()),
                ('transactionNo', models.IntegerField()),
                ('dailyAmount', models.IntegerField()),
                ('paidAmount', models.IntegerField()),
            ],
        ),
    ]
