from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
from .forms import UserRegistrationForm

def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'core/register.html', {'form' : form})
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("announcements_list")
        else:
            return render(request, 'core/register.html', {'form' : form})