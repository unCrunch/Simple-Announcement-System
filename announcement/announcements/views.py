from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Announcement
from .forms import AnnouncementForm
from core.mixins import IsTeacherRoleMixin

@login_required
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/list.html', {'announcements' : announcements})


class AnnouncementListView(LoginRequiredMixin, View):
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

class CreateAnnouncementView(LoginRequiredMixin, IsTeacherRoleMixin, View):
    template_name = 'announcements/create.html'
    form_class = AnnouncementForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()
            return redirect('announcement_list')
        return render(request, self.template_name, {'form' : form})
