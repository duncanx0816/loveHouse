from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('list/', views.ListNote.as_view(), name='list_note'),
]
