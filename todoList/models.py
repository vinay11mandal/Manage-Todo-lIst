from django.db import models
from django_extensions.db.models import TimeStampedModel


class TodoList(TimeStampedModel):
    """Todo List Model contents the list Tasks"""
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField('Active', default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Taks Lists"


class Task(TimeStampedModel):
    """Task Model"""
    STATUS_CATEGORY_CHOICES = (
        (0, 'TODO'),
        (1, 'IN PROGRESS'),
        (2, 'DONE')
    )
    name = models.CharField(max_length=128)
    is_active = models.BooleanField('Active', default=True)
    status = models.IntegerField(verbose_name='Task Status',
        choices=STATUS_CATEGORY_CHOICES, default=0)
    
    description = models.TextField(null=True, blank=True)
    todo_list = models.ForeignKey(TodoList,
        related_name="todo_list", null=True,
        blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Tasks"


class Comment(TimeStampedModel):
    """Comment model for task"""
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField('Active', default=True)
    tasks = models.ForeignKey(Task, related_name="comments",
        null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.is_active)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Comments"
