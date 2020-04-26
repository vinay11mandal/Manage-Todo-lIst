from django.contrib import admin

from todoList.models import (Task, TodoList, Comment)

admin.site.register(Task)
admin.site.register(TodoList)
admin.site.register(Comment)
