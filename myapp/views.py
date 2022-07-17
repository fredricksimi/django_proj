from django.shortcuts import render, redirect
from .forms import *
from .models import UserData
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            telephone_number = form.cleaned_data.get('telephone_number')
            address = form.cleaned_data.get('address')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(
                user=user, first_name=first_name, 
                last_name=last_name, telephone_number=telephone_number,
                address=address
                )
            user_data.save()
            return redirect('created')
    else:
        form = MyCustomSignupForm()
    return render(request, 'myapp/create-account.html', {'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('loggedin')
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={'login_form':form})

def loggedin(request):
    return render(request, 'myapp/loggedin.html')

def logout_view(request):
    logout(request)
    return redirect('loggedout')

def loggedout(request):
    return render(request, 'myapp/loggedout.html')

def createdaccount(request):
    return render(request, 'myapp/created.html')