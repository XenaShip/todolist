from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tasks.apps import TasksConfig
from tasks.views import TaskListApiView, TaskRetrieveApiView, TaskCreateApiView, TaskDestroyApiView, TaskUpdateApiView

app_name = TasksConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # вход
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListApiView.as_view(), name='tasks_list'),
    path('tasks/<int:pk>/', TaskRetrieveApiView.as_view(), name='tasks_retrieve'),
    path('tasks/create/', TaskCreateApiView.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/delete/', TaskDestroyApiView.as_view(), name='tasks_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateApiView.as_view(), name='tasks_update'),
    ]