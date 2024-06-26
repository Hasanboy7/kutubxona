from django.urls import path
from .views import PlasecView,PlacesDetail,UpdatePlace,delete,AddView,CommentView,Error
app_name='places'
urlpatterns=[
    path('list_palces/',PlasecView.as_view(),name='list_palces'),
    path("delete/<int:pk>/",PlacesDetail.as_view(),name='detail'),
    path('update/<int:pk>/',UpdatePlace.as_view(),name='update'),
    path('<int:id>/comment/',CommentView.as_view(),name='comment'),
    path('error/',Error.as_view(),name='error'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('add/',AddView.as_view(),name='add'),

]