from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Place
from .forms import FormPlaces,FormAdd
from django.contrib import messages
# Create your views here.

class PlasecView(View):
    def get(self,request):
        places=Place.objects.all()
        return render(request,'places.html',context={'places':places})

class PlacesDetail(View):
    def get(self,request,pk):
        place=get_object_or_404(Place,pk=pk)

        return render(request,'placedetail.html',context={'place':place})


class UpdatePlace(View):
    def get(self, request, pk):
        place_instance = Place.objects.get(id=pk)
        form = FormPlaces(instance=place_instance)
        return render(request, 'place/update.html', context={'places': form})
    
    def post(self, request, pk):
        place_instance = Place.objects.get(id=pk)
        form = FormPlaces(instance=place_instance, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Muvaffaqiyatli o'zgartirildi")
            return redirect('places:list') 
        return render(request, 'place/update.html', context={'places': form})
    

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
    