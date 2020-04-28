import datetime
from django import forms
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
# Create your models here.

#class Item(models.Model):
    #entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    #item_text = models.CharField('項目', max_length = 200)

class Entry(models.Model):

    today = datetime.date(
                year = timezone.now().year,
                month = timezone.now().month,
                day = timezone.now().day
            )

    pub_date = models.DateField('日期', default = today)
    item = models.CharField('項目', max_length=225)
    entry_type = models.CharField('類別', choices=[('IN','收入'), ('OUT','支出')], default = 'OUT', max_length=5)
    amount = models.IntegerField('金額', validators = [MinValueValidator(0, message = '花費不能是負的')])
    note = models.TextField('備註')
    receipt = models.CharField('收據', max_length = 40)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return str(self.pub_date) + self.item + str(self.amount) + str(self.entry_type)

    def was_published_recently(self):
        return self.pub_date >= today - datetime.timedelta(days=3)
