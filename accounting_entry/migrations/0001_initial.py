# Generated by Django 3.0.5 on 2020-04-24 23:41

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(default=datetime.date(2020, 4, 24), verbose_name='日期')),
                ('item', models.CharField(max_length=200)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='花費不能是負的')])),
                ('is_income', models.BooleanField()),
                ('note', models.TextField()),
                ('receipt', models.CharField(max_length=40)),
            ],
        ),
    ]