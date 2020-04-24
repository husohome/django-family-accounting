from django.shortcuts import render, redirect
from django.http import HttpResponse

def homepage(request):
    #return HttpResponse('home page!')
    return redirect('accounting_entry/')
