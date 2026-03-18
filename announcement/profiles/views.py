from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "GET":
        form = ProfileForm(instance=profile)
    elif request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
        
    return render(request, 'profiles/edit_profile.html', {'form' : form, 'profile' : profile})