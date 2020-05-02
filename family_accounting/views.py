from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def homepage(request):
    #return HttpResponse('home page!')
    return redirect('accounting_entry:homepage')

# Create your views here.
def create_user(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            user = f.save()
            login(request, user)
            return redirect('accounting_entry:homepage')
    else:
        f = UserCreationForm()
    return render(request, 'users/create_user.html', {"f":f})
