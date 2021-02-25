from django.shortcuts import render

def index(request):
    dict = {
        "Task 1": ["10/09/2018", "12/09/2018", "admin", "Done"],
        "Task 2": ["10/09/2018", "12/09/2018", "admin", "Done"],
        "Task 3": ["10/09/2018", "12/09/2018", "admin", "Done"],
        "Task 4": ["10/09/2018", "12/09/2018", "admin", "Done"]
    }
    context={"tasks":dict}
    return render(request,'todo_list.html',context)


def completed(request):
    dict = {
        "Task 0": ["10/09/2018", "12/09/2018", "admin", "Not Done"]
    }
    context = {"tasks": dict}
    return render(request, 'completed_todo_list.html', context)