from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('todos', views.TodoListViewSet, basename='todo')

urlpatterns = router.urls


#urlpatterns = [

    #path('todos/<int:todolist_id>/',views.index,name='index'),
    #path('todos/<int:todolist_id>/completed/',views.completed,name='completed'),
#]