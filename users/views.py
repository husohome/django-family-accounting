from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == "POST":
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            user = f.get_user()
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('accounting_entry:homepage')
            else:
                return HttpResponse('login failed')
    else:
        f = AuthenticationForm()
    return render(request, 'users/login.html', {'f':f})

def logout_user(request):
    if request.method == 'POST':
        # log out the user
        logout(request) # since the user is already logged in
        return redirect('accounting_entry:homepage')
