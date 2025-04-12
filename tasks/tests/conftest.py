import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user():
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def test_task(test_user):
    return Task.objects.create(
        user=test_user,
        title='Test Task',
        description='Test Description',
        completed=False
    )