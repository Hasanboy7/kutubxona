from django.shortcuts import render
from place.models import Place,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
def landing_page(request):
    return  render(request,'landing.html')

class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        place=Comment.objects.exclude(user=request.user)
        return  render(request,'landing.html',context={'place':place})
