from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def homepage(request):
    #return HttpResponse('home page!')
    return redirect('accounting_entry:homepage')

# Create your views here.
def create_user(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            login(request, user)
            return redirect('accounting_entry:homepage')
    else:
        f = UserCreationForm()
    return render(request, 'users/create_user.html', {"f":f})

def login_user(request):
    if request.method == "POST":
        f = AuthenticationForm(request.POST)
        if f.is_valid():
            user = form.get_user()
            login(reqeust, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounting_entry:homepage')
    else:
        f = AuthenticationForm()
        return render(request, 'users/login.html', {'f':f})


def logout_view(request):
    if request.method == 'POST':
        # log out the user
        logout(request) # since the user is already logged in
        return redirect('articles:list')
