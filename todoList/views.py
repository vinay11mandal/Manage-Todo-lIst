from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from todoList.models import (Task, TodoList, Comment)
from rest_framework.response import Response
from rest_framework import status
from todoList.serializers import (AddTaskSerializer,
	AddTodoListSerializer, AddCommentSerializer, AddOnlyTaskSerializer)


class AddTaskViewSet(viewsets.ModelViewSet):
    """
    API to create a Task and assign to list
    """
    serializer_class = AddTaskSerializer
    queryset = Task.objects.all()

    def create(self, request):
        """Post method"""
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


class AddOnlyTask(CreateAPIView):
    """Add only task"""
    queryset = Task.objects.all()
    serializer_class = AddOnlyTaskSerializer

    def create(self, request, format='json'):
        """docstring"""
        params = request.data
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'data' : serializer.data,
            'message': 'Task is created successfully.',
            }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """docstring"""
        serializer.save()

