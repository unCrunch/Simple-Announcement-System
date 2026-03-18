from django.urls import path
from .views import update_profile

urlpatterns = [
    path("edit/", update_profile, name='edit_profile')
]