
from django.urls import path
from .views import (register,LogInView,LogOut,
                    UpdateView,Profil,ResetPasswordView,
                    UserView,SendRequest,MyNetworksView,Accsept,Ignore,Delet)

app_name="users"

urlpatterns=[
    path('register/',register,name="register"),
    path('login/',LogInView.as_view(),name="login"),
    path('logout/',LogOut.as_view(),name="logout"),
    path('update/', UpdateView.as_view(), name="update"),
    path('profil/<int:pk>/', Profil.as_view(), name="profil"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset_password"),

    # users freand request
    path('list/',UserView.as_view(),name='list'),
    path('send_request/<int:id>/',SendRequest.as_view(),name='send'),
    path('networks/',MyNetworksView.as_view(),name='networks'),
    path('accept-friend/<int:id>/',Accsept.as_view(),name='accept'),
    path('ignore-ignor/<int:id>/',Ignore.as_view(),name='ignore'),
    path('delete-friend/<int:id>/',Delet.as_view(),name='delete'),
]