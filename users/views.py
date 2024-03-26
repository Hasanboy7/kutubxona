from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm,LoginForm,UpdateForm
# Create your views here.
# class RegisterView(FormView):
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.info(request,"Registratsadan muffaqyatli o'ttingiz")
            return redirect('users:login')  # Redirect to login page or wherever you want
       

    return render(request, 'users/register.html', context={'form': form})


class LogInView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login.html',context={'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username)

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Sayitga maffaqyatli tashrif buyurdingiz')
                return redirect('landing_page')

        return render(request,'users/login.html',context={'form':form})

class LogOut(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'Sayitdan chiqib ketingiz')
        return redirect('landing_page')

class UpdateView(LoginRequiredMixin,View):
    def get(self,request):
        form=UpdateForm(instance=request.user)
        return render(request,'users/update.html',context={'form':form})
    def post(self,request):
        form =UpdateForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request,"Mufaqyatli O'zgartirildi")
            return redirect('landing_page')

        return render(request, 'users/update.html', context={'form': form})