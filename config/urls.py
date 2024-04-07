

from django.contrib import admin
from django.urls import path,include
from .view import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(),name="landing_page"),
    path("user/",include('users.urls')),
    path("places/",include('place.urls')),
    path("api/",include('api.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
