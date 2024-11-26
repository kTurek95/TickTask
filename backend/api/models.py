from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='task_created', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='task_updated', on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField()
    completed_by = models.ForeignKey(User, related_name='taks_completed', on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


