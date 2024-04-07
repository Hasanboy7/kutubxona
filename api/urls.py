from django.urls import path
from .views import ListTodo,ListCreate,ListTodos,CommentView,UserView

app_name='api'
urlpatterns = [
    # Place
    path('place-api/',ListTodos.as_view(),name='lists-api'),
    path('place-api/<int:pk>/',ListTodo.as_view(),name='list-api'),
    path('place-create/',ListCreate.as_view(),name='list-create'),

    # Comment
    path('comment-api/',CommentView.as_view(),name='comment_app'),
    # User
    path('user/',UserView.as_view(),name='user'),
]
