# Generated by Django 3.0.5 on 2020-04-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_entry', '0006_auto_20200427_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='entry',
        ),
        migrations.AddField(
            model_name='entry',
            name='item',
            field=models.ManyToManyField(to='accounting_entry.Item'),
        ),
    ]
