from django.shortcuts import render
from main.models import TodoList,Task
from rest_framework import generics, mixins, viewsets
from main.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


# def index(request,todolist_id):
#     todolist=TodoList.objects.get(id=todolist_id)
#     tasks=Task.objects.filter(todolist=todolist,mark=False)
#     context={
#         "todolist":todolist,
#         "done_tasks":tasks
#     }
#     return render(request,'todo_list.html',context)
#
#
# def completed(request,todolist_id):
#     todolist = TodoList.objects.get(id=todolist_id)
#     completed_tasks = Task.objects.filter(todolist=todolist, mark=True)
#     context = {
#         "completed_tasks": completed_tasks,
#         "todolist": todolist
#     }
#     return render(request, 'completed_todo_list.html', context)


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

