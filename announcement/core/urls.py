from django.urls import path
from django.contrib.auth import views as auth
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
]