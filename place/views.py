from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.views import View
from .models import Place,Comment
from .forms import FormPlaces,FormAdd,CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PlasecView(View):
    def get(self,request):
        places=Place.objects.all()
        search_query=request.GET.get('q','')
        if search_query:
            places=places.filter(name__icontains=search_query)
        
        return render(request,'places.html',context={'places':places,"search_query":search_query})


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
    
# class AddView(View):
#     def get(self,request):
#         form=FormAdd()
#         return render(request, 'place/add.html', context={'form': form})
#     def post(self,request):
#         if request.method=='POST':
#             print(request.POST)
#             form=FormAdd(request.POST,files=request.FILES)
#             if form.is_valid():
#                 form.save()
#                 messages.warning(request, "Muvaffaqiyatli saqlandi")
#                 return redirect('places:list')
#         return render(request, 'place/add.html', context={'form': form})


def delete(request, pk):
    place_instance = get_object_or_404(Place, id=pk)
    place_instance.delete()
    return redirect('places:list')

class CommentView(LoginRequiredMixin,View):
    def post(self,request,id):
        place=Place.objects.get(id=id)
        form=CommentForm(request.POST)
        if form.is_valid():  
            Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                stars_give=form.cleaned_data['stars_give']
            )
            return redirect(reverse('places:detail',kwargs={'pk':place.id}))
        return render(request,'placedetail.html',context={'place':place,'form':form})