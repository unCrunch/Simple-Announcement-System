from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views import View
from django.utils.decorators import method_decorator
from .models import Announcement
from .forms import AnnouncementForm

# Create your views here.

@login_required
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/list.html', {'announcements' : announcements})



@method_decorator(login_required, name='dispatch')
class AnnouncementListView(View):
    template_name = 'announcements/list.html'
    
    def get(self, request):
        announcements = Announcement.objects.all()
        return render(request, self.template_name, {'announcements' : announcements})

def is_teacher(user):
    return user.role == 'teacher'

@login_required
# using manual role added into user model
# @user_passes_test(is_teacher, login_url='login')
@permission_required('announcements.add_announcement', raise_exception=True)
def create_announcement(request):
    if request.method == "GET":
        form = AnnouncementForm()
        return render(request, 'announcements/create.html', {'form' : form})
    elif request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()
            form_data = {
                'form' : AnnouncementForm(),
                'new_announcement' : announcement,
                'success' : True
            }
            return render(request, 'announcements/create.html', form_data)
        else:
            return render(request, 'announcements/create.html', {'form' : form})

