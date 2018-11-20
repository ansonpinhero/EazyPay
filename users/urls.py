# users/urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
]