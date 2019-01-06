from django.urls import path
from . import views

app_name = 'wish'

urlpatterns = [
    path('list/', views.ListWish.as_view(), name='list_wish'),
    path('new/', views.NewWish.as_view(), name='new_wish'),
]
