
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
from .models import User,FriendRequest

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
    

class UserView(LoginRequiredMixin,View):
    def get(self,request):
        users_list=User.objects.exclude(username=request.user.username)
        firend_request=User.objects.filter(id__in=FriendRequest.objects.filter(form_user=request.user).values_list('to_user'))
        return render(request,'users/user_list.html',context={'users_list':users_list,'firend_request':firend_request})


class MyNetworksView(LoginRequiredMixin,View):
    def get(self,request):
        networks=FriendRequest.objects.filter(to_user=request.user,is_accepted=False)
        return render(request,'users/networks_list.html',context={'networks':networks})


class Accsept(LoginRequiredMixin,View):
    def get(selft,request,id):
        frend_request=FriendRequest.objects.get(id=id)
        form_user=frend_request.form_user
        main_user=request.user

        main_user.firends.add(form_user)
        # main_user.firends.add(main_user)

        frend_request.is_accepted=True
        frend_request.save()
        return redirect('users:networks')


class Ignore(LoginRequiredMixin,View):
    def get(self,request,id):
        friend_request=FriendRequest.objects.get(id=id)
        friend_request.delete()
        return redirect('users:networks')
    
class Delet(LoginRequiredMixin,View):
    def get(self,request,id):
        friend=User.objects.get(id=id)
        user=request.user
        user.firends.remove(friend)
        friend.firends.remove(user)
        return redirect('users:list')
    

class SendRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        to_user = User.objects.get(id=id)
        form_user = request.user
        FriendRequest.objects.get_or_create(form_user=form_user,to_user=to_user)
        return redirect('users:list')