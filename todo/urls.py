from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.ListTodo.as_view(), name='list_todo'),
    path('new/', views.NewTodo.as_view(), name='new_todo'),
]
