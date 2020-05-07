from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import modelformset_factory
from .models import Entry
from .forms import EntryForm
import pandas as pd
from django.contrib.auth.decorators import login_required
from numpy import nan

# Create your views here.
@login_required(login_url="users:login_user")
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
        'receipt': [e.receipt for e in total_entries],
        'author': [e.author.username if e.author.username != "husohome" else nan for e in total_entries]
        }
    )

    xtab = pd.crosstab([df['年'], df['月']], df['author'], values=df['支出'], aggfunc=sum,margins=True).reset_index()
    xtab.columns.name=None
    xtab.fillna(0)

    income = df['收入'].sum().astype(int)
    expenditure = df['支出'].sum().astype(int)
    context  = {
        'total_income': income,
        'total_expenditure': expenditure,
        'total_entries': total_entries,
        'amount_left': income - expenditure,
        'df': df.to_html(),
        'df_by_month': df.groupby(['年', '月'])[['收入','支出']].sum().reset_index().to_html(),
        'xtab': xtab.to_html(),
    }
    return render(request, 'accounting_entry/summary.html', context)

@login_required(login_url="users:login_user")
def detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.author == request.user:
        return HttpResponseRedirect(reverse('accounting_entry:edit', args=(entry_id,)))
    return render(request, 'accounting_entry/detail.html', {'entry':entry})

@login_required(login_url="users:login_user")
def edit_entry(request, entry_id):
    if request.user != Entry.objects.get(id=entry_id).author:
        return HttpResponseRedirect(reverse('accounting_entry:detail', args=(entry_id,)))
    else:
        EntryFormSet = modelformset_factory(
            Entry,
            exclude = ('author', ),
            extra = 0,
            can_delete=True
        )
        if request.method == 'POST':
            f = EntryFormSet(request.POST, queryset=Entry.objects.filter(author=request.user,id=entry_id))
            if f.is_valid():
                instances = f.save(commit=True)
                return HttpResponseRedirect(reverse('accounting_entry:homepage'))
        else:
            f = EntryFormSet(queryset=Entry.objects.filter(author=request.user,id=entry_id))
    return render(request, 'accounting_entry/manage_entries.html', {'f':f, 'f_len':len(f)>0, 'edit_mode':True})

@login_required(login_url="users:login_user")
def add_entry(request):
    if request.method == 'POST':
        f = EntryForm(request.POST)
        if f.is_valid():
            # save article to db
            instance = f.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse('accounting_entry:homepage'))
    else:
        #items = list(set([(e.item, e.item) for e in Entry.objects.all()]))
        #if len(items) == 0:
        #    items = [("新增","新增")]
        f = EntryForm()
        #f.Meta.widgets = {"item": Select(choices = items)}
        #return HttpResponse(items)
        return render(request, 'accounting_entry/add_entry.html', {'f':f})

# manage all instances --- maybe add user functionality
@login_required(login_url="users:login_user")
def manage_entries(request):
    EntryFormSet = modelformset_factory(
        Entry,
        exclude = ('author', ),
        extra = 0,
        can_delete=True
    )
    if request.method == 'POST':
        f = EntryFormSet(request.POST, queryset=Entry.objects.filter(author=request.user).order_by('-pub_date'))
        if f.is_valid():
            # save article to db
            instances = f.save(commit=True)
            #for instance in instances:
            #    instance.author = request.user
            #    instance.save()
            return HttpResponseRedirect(reverse('accounting_entry:homepage'))
    else:
        #items = list(set([(e.item, e.item) for e in Entry.objects.all()]))
        #if len(items) == 0:
        #    items = [("新增","新增")]
        f = EntryFormSet(queryset=Entry.objects.filter(author=request.user).order_by('-pub_date'))

        #f.Meta.widgets = {"item": Select(choices = items)}
        #return HttpResponse(items)
    return render(request, 'accounting_entry/manage_entries.html', {'f':f, 'f_len':len(f)>0})
