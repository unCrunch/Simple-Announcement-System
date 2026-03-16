from django.urls import path
from django.contrib.auth import views as auth
from .views import register, custom_login

urlpatterns = [
    path('register/', register, name='register'),
    # using built in login:
    path('login/', auth.LoginView.as_view(template_name='core/login.html'), name='login'),
    #using custom login:
    # path('login/', custom_login, name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
]