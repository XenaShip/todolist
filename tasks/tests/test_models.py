from django.contrib.auth.models import User
import pytest
from tasks.models import Task


@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    task = Task.objects.create(
        user=user,
        title='Test Task',
        description='Test Description',
        completed=False
    )
    assert task.title == 'Test Task'
    assert task.user == user
    assert str(task) == 'Test Task'
    assert task.description == 'Test Description'
    assert task.completed == False