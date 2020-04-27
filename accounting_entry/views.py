from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entry
from .forms import EntryForm
import pandas as pd

# Create your views here.
def summary_page(request):
    total_entries = Entry.objects.order_by('-pub_date')
    df = pd.DataFrame(
        {'ID': [e.id for e in total_entries],
        'pub_date': [e.pub_date for e in total_entries],
        'year': [e.pub_date.year for e in total_entries],
        'month': [e.pub_date.month for e in total_entries],
        'amount': [e.amount if e.entry_type=='in' else e.amount*(-1) for e in total_entries],
        'note': [e.note for e in total_entries],
        'receipt': [e.receipt for e in total_entries]
        }
    )

    income = pd.Series([e.amount for e in Entry.objects.filter(entry_type='in')]).sum().astype(int)
    expenditure = pd.Series([e.amount for e in Entry.objects.filter(entry_type='out')]).sum().astype(int)
    context  = {
        'total_income': income,
        'total_expenditure': expenditure,
        'total_entries': total_entries,
        'amount_left': income - expenditure,
        'df': df.to_html(),
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
            instance.author = request.user
            instance.save()
            return redirect('accounting_entry:homepage')
    else:
        f = EntryForm()
        return render(request, 'accounting_entry/add_entry.html', {'f': f})
