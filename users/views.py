
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm,LoginForm,UpdateForm,ResetPassword
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.info(request, "Registratsadan muffaqyatli o'ttingiz")
            return redirect('users:login')
    else:
        form = RegisterForm()
       
    return render(request, 'users/register.html', context={'form': form})

class Profil(View):
    def get(self,request,pk):
        return render(request,'users/profil.html')

class LogInView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login.html',context={'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
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
        if request.method=='POST':
            form =UpdateForm(instance=request.user,data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.warning(request,"Mufaqyatli O'zgartirildi")
                return redirect('landing_page')

        return render(request, 'users/update.html', context={'form': form})
    

class ResetPasswordView(LoginRequiredMixin,View):
    def get(self,request):
        form=ResetPassword()
        return render(request,'users/reset_password.html',context={'form':form})
    
    def post(self,request):
        form=ResetPassword(request.POST)
        user=request.user
        if form.is_valid():
            if check_parol(user,form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['password_config'])
                user.save()
                return redirect('users:login')
            else:
                return render(request,'users/reset_password.html',context={'form':form})
            
        return render(request,'users/reset_password.html',context={'form':form})


def check_parol(user,password):
    return user.check_password(password)
    