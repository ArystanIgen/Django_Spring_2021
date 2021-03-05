from django.db import models
from django.contrib.auth.models import User



class TodoList(models.Model):
    list_name=models.CharField(max_length=255)

    class Meta:
        verbose_name = "Список"
        verbose_name_plural = "Списки"

    def __str__(self):
        return self.list_name

class Task(models.Model):
    todolist=models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="tasks")
    goal=models.TextField("Task")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Добавлен")
    due_on=models.DateTimeField(verbose_name="Выполнить к")
    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Владелец")
    mark=models.BooleanField(default=False,verbose_name="Cтатус")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.goal