from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib import messages



def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout success!')
    return redirect('home')



