from rest_framework import serializers
from todoList.models import (Task, TodoList, Comment) 


class AddTaskSerializer(serializers.ModelSerializer):
    """Model Serializer for Task with specific fields"""

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'status',
            'description',
            'todo_list',
            'created',
            'modified'
        ]
        read_only_fields = ['id', 'created', 'modified']


class AddTodoListSerializer(serializers.ModelSerializer):
    """Model Serializer for Task """

    class Meta:
        model = TodoList
        fields = [
            'id',
            'name',
            'description',
            'start_date',
            'end_date',
            'created',
            'modified'
        ]
        read_only_fields = ['id', 'created', 'modified']


class AddCommentSerializer(serializers.ModelSerializer):
    """Model Serializer for Comment"""

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'tasks',
            'created',
            'modified'
        ]
        read_only_fields = ['id', 'created', 'modified']

class AddOnlyTaskSerializer(serializers.ModelSerializer):
    """Model Serializer for Task with specific fields"""

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'status',
            'description',
            'created',
            'modified'
        ]
        read_only_fields = ['id', 'created', 'modified']

