from django.urls import (path, include)
from rest_framework.routers import DefaultRouter
from todoList import views

router = DefaultRouter()
router.register(r'task', views.AddTaskViewSet, basename='task')
router.register(r'todo-list', views.AddTodoListViewSet, basename='todo-list')
router.register(r'comment', views.AddCommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
]
