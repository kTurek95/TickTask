from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskListCreate.as_view(), name='task-list'),
    path('tasks/delete/<int:pk>/', views.TaskDelete.as_view(), name='delete-task'),

]