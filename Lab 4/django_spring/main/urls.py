
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [

    path('todos/<int:todolist_id>/',views.index,name='index'),
    path('todos/<int:todolist_id>/completed/',views.completed,name='completed'),
]