from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import UserRegisterForm
from django.contrib.auth.models import User 


class UserRegisterView(View):
    """cbv for registering users"""
    class_form = UserRegisterForm
    template_adrs= 'accounts/register.html'
    
    def get(self, request):
        return render(request, 'home/home.html', {'register_form':self.class_form})
    
    def post(self, request):
        register_form = self.class_form(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            return redirect('home:home')
        
        return render(request, self.template_adrs,{'register_form':register_form})
    