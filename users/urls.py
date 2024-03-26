from django.urls import path
from .views import register,LogInView,LogOut,UpdateView

app_name="users"

urlpatterns=[
    path('register/',register,name="register"),
    path('login/',LogInView.as_view(),name="login"),
    path('logout/',LogOut.as_view(),name="logout"),
    path('update/', UpdateView.as_view(), name="update"),
]