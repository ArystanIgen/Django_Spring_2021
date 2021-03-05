from django.contrib import admin
from .models import TodoList,Task
# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ['list_name']
    search_fields = ['list_name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['goal', 'created', 'due_on', 'mark']
    search_fields = ['goal']


admin.site.register(Task,TaskAdmin)
admin.site.register(TodoList,TodoListAdmin)
