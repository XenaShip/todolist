from django.urls import path
from tasks.apps import TasksConfig
from tasks.views import TaskListApiView, TaskRetrieveApiView, TaskCreateApiView, TaskDestroyApiView, TaskUpdateApiView

app_name = TasksConfig.name

urlpatterns = [
    path('tasks/', TaskListApiView.as_view(), name='tasks_list'),
    path('tasks/<int:pk>/', TaskRetrieveApiView.as_view(), name='tasks_retrieve'),
    path('tasks/create/', TaskCreateApiView.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/delete/', TaskDestroyApiView.as_view(), name='tasks_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateApiView.as_view(), name='tasks_update'),
    ]