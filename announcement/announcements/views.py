from django.shortcuts import render
from .models import Announcement
from .forms import AnnouncementForm

# Create your views here.

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/list.html', {'announcements' : announcements})

def create_announcement(request):
    if request.method == "GET":
        form = AnnouncementForm()
        return render(request, 'announcements/create.html', {'form' : form})
    elif request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            announcement = form.instance
            form_data = {
                'form' : AnnouncementForm(),
                'new_announcement' : announcement,
                'success' : True
            }
            return render(request, 'announcements/create.html', form_data)
        else:
            return render(request, 'announcements/create.html', {'form' : form})

