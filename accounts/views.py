from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from home.views import home_view

# Create your views here.
def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect(home_view)
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect(home_view)
    context['form'] = form
    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            return redirect(login_view)
        return render(request, 'accounts/logout.html', context=context)
    return redirect(home_view)