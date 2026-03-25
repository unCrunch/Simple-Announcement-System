from django.urls import path
from .views import announcement_list, create_announcement, AnnouncementListView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcements_list'),
    path('create/', create_announcement, name='create_announcement'),
]