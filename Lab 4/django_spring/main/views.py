from django.shortcuts import render
from .models import TodoList,Task
def index(request,todolist_id):
    todolist=TodoList.objects.get(id=todolist_id)
    tasks=Task.objects.filter(todolist=todolist,mark=False)
    context={
        "todolist":todolist,
        "done_tasks":tasks
    }
    return render(request,'todo_list.html',context)


def completed(request,todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    completed_tasks = Task.objects.filter(todolist=todolist, mark=True)
    context = {
        "completed_tasks": completed_tasks,
        "todolist": todolist
    }
    return render(request, 'completed_todo_list.html', context)