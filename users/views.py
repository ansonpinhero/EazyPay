# users/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import CustomUserCreationForm
from django.shortcuts import render_to_response, redirect , render
from django.template import RequestContext
#class SignUp(generic.CreateView):
 #   form_class = CustomUserCreationForm
 #   success_url = reverse_lazy('login')
 #   template_name = 'signup.html'

def check_admin(request):
   return request.user.is_superuser
@login_required(login_url = '/users/login/')
#@user_passes_test(check_admin)
def SignUp(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                #username = form.cleaned_data.get('username')
                #raw_password = form.cleaned_data.get('password1')
                #user = authenticate(username=username, password=raw_password)
                #login(request, user)
                return redirect('home')
        else:
            form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'unauthorized.html')
        
    
@login_required(login_url = '/users/login/')    
def Dashboard(request):
    return render(request, 'home.html', {})