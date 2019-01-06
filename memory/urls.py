from django.urls import path
from . import views

app_name = 'memory'

urlpatterns = [
    path('index/', views.MemoryIndex.as_view(), name='memory_index'),
]
