from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entry
from .forms import EntryForm, EntryFormSet
import pandas as pd

# Create your views here.
def summary_page(request):
    total_entries = Entry.objects.order_by('-pub_date')
    df = pd.DataFrame(
        {'ID': [e.id for e in total_entries],
        'pub_date': [e.pub_date for e in total_entries],
        '年': [e.pub_date.year for e in total_entries],
        '月': [e.pub_date.month for e in total_entries],
        '收入': [e.amount if e.entry_type=='IN' else 0 for e in total_entries],
        '支出': [e.amount if e.entry_type=='OUT' else 0 for e in total_entries],
        'note': [e.note for e in total_entries],
        'receipt': [e.receipt for e in total_entries]
        }
    )

    income = df['收入'].sum().astype(int)
    expenditure = df['支出'].sum().astype(int)
    context  = {
        'total_income': income,
        'total_expenditure': expenditure,
        'total_entries': total_entries,
        'amount_left': income - expenditure,
        'df': df.to_html(),
        'df_by_month': df.groupby(['年', '月'])[['收入','支出']].sum().to_html(),
    }
    return render(request, 'accounting_entry/summary.html', context)

def detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render(request, 'accounting_entry/detail.html', {'entry':entry})

def add_entry(request):
    if request.method == 'POST':
        f = EntryForm(request.POST)
        if f.is_valid():
            # save article to db
            instance = f.save(commit=False)
            #instance.author = request.user
            instance.save()
            return redirect('accounting_entry:homepage')
    else:
        #items = list(set([(e.item, e.item) for e in Entry.objects.all()]))
        #if len(items) == 0:
        #    items = [("新增","新增")]
        f = EntryForm()
        #f.Meta.widgets = {"item": Select(choices = items)}
        #return HttpResponse(items)
        return render(request, 'accounting_entry/add_entry.html', {'f':f})

# manage all instances --- maybe add user functionality
def manage_entries(request):
    if request.method == 'POST':
        f = EntryFormSet(request.POST)
        if f.is_valid():
            # save article to db
            instances = f.save(commit=False)
            for instance in instances:
                #instance.author = request.user
                instance.save()
            return redirect('accounting_entry:homepage')
    else:
        #items = list(set([(e.item, e.item) for e in Entry.objects.all()]))
        #if len(items) == 0:
        #    items = [("新增","新增")]
        f = EntryFormSet()
        #f.Meta.widgets = {"item": Select(choices = items)}
        #return HttpResponse(items)
        return render(request, 'accounting_entry/manage_entries.html', {'f':f})
