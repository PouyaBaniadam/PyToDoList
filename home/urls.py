from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
    path('completed-task/<int:task_id>/', views.completed_task, name='completed-task'),
    path('undo-task/<int:task_id>/', views.undo_completed_task, name='undo-task'),
    path('<str:status>', views.filter_tasks, name='filter-tasks'),

]