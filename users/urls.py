
from django.urls import path
from .views import register,LogInView,LogOut,UpdateView,Profil,ResetPasswordView

app_name="users"

urlpatterns=[
    path('register/',register,name="register"),
    path('login/',LogInView.as_view(),name="login"),
    path('logout/',LogOut.as_view(),name="logout"),
    path('update/', UpdateView.as_view(), name="update"),
    path('profil/<int:pk>/', Profil.as_view(), name="profil"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset_password"),
]