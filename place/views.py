from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.views import View
from .models import Place,Comment,FirendRequest
from .forms import FormPlaces,FormAdd,CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User
# Create your views here.

# comment add users 
class PlasecView(View):
    def get(self,request):
        places=Place.objects.all()
        search_query=request.GET.get('q','')
        if search_query:
            places=places.filter(name__icontains=search_query)
        
        return render(request,'places.html',context={'places':places,"search_query":search_query})

# batafsil o'qish
class PlacesDetail(View):
    def get(self,request,pk):
        form=CommentForm()
        place=get_object_or_404(Place,id=pk)
        return render(request,'placedetail.html',context={'place':place,'form':form})

class UpdatePlace(View):
    def get(self, request, pk):
        place_instance = Place.objects.get(id=pk)
        form = FormPlaces(instance=place_instance)
        return render(request, 'place/update.html', context={'places': form})
    
    def post(self, request,pk):
        place_instance = Place.objects.get(id=pk)
        form = FormPlaces(instance=place_instance, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Muvaffaqiyatli o'zgartirildi")
            return redirect('places:list') 
        return render(request, 'place/update.html', context={'forms': form})
    

def AddView(request):
    form = FormAdd()
    if request.method=='POST':
        form = FormAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, "Muvaffaqiyatli saqlandi")
            return redirect('places:list')
    return render(request, 'place/add.html', context={'form': form})
    
def delete(request, pk):
    place_instance = get_object_or_404(Place, id=pk)
    place_instance.delete()
    return redirect('places:list')

class Error(View):
    def get(self,request):
        return render(request,'error.html')
    
class CommentView(LoginRequiredMixin,View):
    def get(self,request):
        comment=Comment.objects.all()
        return render(request,'landing.html',context={'comment':comment})
    def post(self,request,id):
        place=Place.objects.get(id=id)
        form=CommentForm(request.POST)
        if form.is_valid():  
            try:
                comment=Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                stars_give=form.cleaned_data['stars_give']
                )
            except:
                # raise Exception('Bunday maydon mavjut')
                return redirect('places:error')
            comment.save()
            return redirect(reverse('places:detail',kwargs={'pk':place.id}))
        
        return render(request,'placedetail.html',context={'place':place,'form':form})
    

# Do'slarga recoment tashlash
    
class UserView(LoginRequiredMixin,View):
    def get(self,request):
        users_list=User.objects.exclude(username=request.user.username)

        return render(request,'users/user_list.html',context={'users_list':users_list})


class MyNetworksView(LoginRequiredMixin,View):
    def get(self,request):
        networks=FirendRequest.objects.filter(to_user=request.user,is_accepted=False)
        return render(request,'networks_list.html',context={'networks':networks})


class Accsept(LoginRequiredMixin,View):
    def get(selft,request,id):
        frend_request=FirendRequest.objects.get(id=id)
        from_user=frend_request.from_user

        main_user=request.user
        main_user.friends.add(from_user)

class SendRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        to_user = User.objects.get(id=id)
        from_user = request.user

        FirendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        return redirect('places:users')



