# Generated by Django 3.0.5 on 2020-04-25 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_entry', '0003_auto_20200424_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_type',
            field=models.CharField(choices=[('IN', '收入'), ('OUT', '支出')], default='OUT', max_length=5, verbose_name='支出/收入'),
        ),
    ]
