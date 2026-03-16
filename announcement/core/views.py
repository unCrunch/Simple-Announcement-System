from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group

# Create your views here.
from .forms import UserRegistrationForm
from .models import User


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'core/register.html', {'form' : form})
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == 'teacher':
                teacher_group = Group.objects.get(name='Teacher')
                user.groups.add(teacher_group)
            elif user.role == 'student':
                student_group = Group.objects.get(name='Student')
                user.groups.add(student_group)
            user.save()
            login(request, user)
            return redirect("announcements_list")
        else:
            return render(request, 'core/register.html', {'form' : form})

# will not be used in this program, but it is shown so that it is understood i can create basic custom login pages
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('announcements_list')
    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form' : form})