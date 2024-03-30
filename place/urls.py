from django.urls import path
from .views import PlasecView,PlacesDetail,UpdatePlace,delete,AddView,CommentView
app_name='places'
urlpatterns=[
    path('list/',PlasecView.as_view(),name='list'),
    path("list/<int:pk>/",PlacesDetail.as_view(),name='detail'),
    path('update/<int:pk>/',UpdatePlace.as_view(),name='update'),
    path('<int:id>/comment/',CommentView.as_view(),name='comment'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('add/',AddView,name='add'),
]