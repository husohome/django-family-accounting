# Generated by Django 3.0.5 on 2020-04-25 02:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='花費不能是負的')], verbose_name='金額'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='is_income',
            field=models.BooleanField(verbose_name='若是收入則打勾，若是支出則不要打勾'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='item',
            field=models.CharField(max_length=200, verbose_name='項目'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='note',
            field=models.TextField(verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='receipt',
            field=models.CharField(max_length=40, verbose_name='收據'),
        ),
    ]
