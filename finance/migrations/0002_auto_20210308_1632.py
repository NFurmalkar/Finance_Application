# Generated by Django 3.1.4 on 2021-03-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmodel',
            name='Amountfinal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='Udays',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='chequeNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='interest',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='interestAmount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='paidAmount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='todayDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='loanmodel',
            name='transactionNo',
            field=models.IntegerField(),
        ),
    ]
