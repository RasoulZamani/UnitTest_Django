from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(sel,request):
        return render(request, 'home/home.html')