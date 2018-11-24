# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
]