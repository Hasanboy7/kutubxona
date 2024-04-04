from django.urls import path
from .views import PlasecView,PlacesDetail,UpdatePlace,MyNetworksView,SendRequest,UserView,delete,AddView,CommentView,Error
app_name='places'
urlpatterns=[
    path('list/',PlasecView.as_view(),name='list'),
    path("list/<int:pk>/",PlacesDetail.as_view(),name='detail'),
    path('update/<int:pk>/',UpdatePlace.as_view(),name='update'),
    path('<int:id>/comment/',CommentView.as_view(),name='comment'),
    path('error/',Error.as_view(),name='error'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('add/',AddView,name='add'),
    path('users/',UserView.as_view(),name='users'),

    # users freand request
    path('send_request/<int:id>/',SendRequest.as_view(),name='send'),
    path('networks/',MyNetworksView.as_view(),name='networks')
]