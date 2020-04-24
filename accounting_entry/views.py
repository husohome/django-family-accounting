from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def summary_page(request):
    #return HttpResponse('Hi! You have called the function summary_page')
    return render(request, 'accounting_entry/accounting_summary.html')
