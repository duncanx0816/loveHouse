from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('list/', views.ListNote.as_view(), name='list_note'),
    path('new/', views.NewNote.as_view(), name='new_note'),
    path('history/', views.HistNote.as_view(), name='hist_note'),
]
