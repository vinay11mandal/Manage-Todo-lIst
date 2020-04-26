from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from todoList.models import (Task, TodoList, Comment)
from rest_framework.response import Response
from rest_framework import status
from todoList.serializers import (AddTaskSerializer,
	AddTodoListSerializer, AddCommentSerializer)


class AddTaskViewSet(viewsets.ModelViewSet):
    """
    API to create a Task and assign to list
    """
    serializer_class = AddTaskSerializer
    queryset = Task.objects.all()

    def create(self, request):
        """
        To add just task pass enpty string to todo_list
        To add task to todolist pass id of todolist
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            task = serializer.save()

            return Response({
                'data' : self.serializer_class(task).data,
                'message': 'Task is created successfully.',
            }, status.HTTP_201_CREATED,)


class AddTodoListViewSet(viewsets.ModelViewSet):
    """
    API to create a Todo List
    """
    serializer_class = AddTodoListSerializer
    queryset = TodoList.objects.all()

    def create(self, request):
        """Post method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            todo_list = serializer.save()

            return Response({
                'data' : self.serializer_class(todo_list).data,
                'message': 'Todo List is created successfully.',
            }, status.HTTP_201_CREATED,)


class AddCommentViewSet(viewsets.ModelViewSet):
    """
    API to add a comment
    """
    serializer_class = AddCommentSerializer
    queryset = Comment.objects.all()

    def create(self, request):
        """Post method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()

            return Response({
                'data' : self.serializer_class(comment).data,
                'message': 'Todo List is created successfully.',
            }, status.HTTP_201_CREATED,)


