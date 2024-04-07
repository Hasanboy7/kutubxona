from django.urls import path
from .views import ListTodo,ListCreate,ListTodos

app_name='api'
urlpatterns = [
    path('list-api/',ListTodos.as_view(),name='lists-api'),
    path('list-api/<int:pk>/',ListTodo.as_view(),name='list-api'),
    path('list-create/',ListCreate.as_view(),name='list-create'),
]
