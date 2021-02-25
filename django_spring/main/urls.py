
from django.urls import path
from . import views
urlpatterns = [

    path('todos/',views.index,name='index'),
    path('todos/1/completed/',views.completed,name='completed'),
]