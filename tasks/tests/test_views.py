import pytest
from django.urls import reverse

from tasks.models import Task


@pytest.mark.django_db
def test_task_create(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    create_data = {
        'title': 'New Task',
        'description': 'New Description',
        'completed': False
    }
    create_url = reverse('tasks:tasks_create')
    create_response = api_client.post(create_url, create_data, format='json')

    assert create_response.status_code == 201
    assert create_response.data['title'] == 'New Task'
    assert create_response.data['user'] == test_user.id

    task_id = create_response.data['id']
    data_update = {
        'title': 'old Task',
        'description': 'New Description',
        'completed': False
    }
    url = reverse('tasks:tasks_update', kwargs={'pk': task_id})
    response = api_client.put(url, data_update, format='json')
    assert response.status_code == 200
    assert response.data['title'] == 'old Task'


@pytest.mark.django_db
def test_task_list(api_client, test_user, test_task):
    api_client.force_authenticate(user=test_user)

    url = reverse('tasks:tasks_list')
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['title'] == 'Test Task'


@pytest.mark.django_db
def test_task_delete(api_client, test_user, test_task):
    api_client.force_authenticate(user=test_user)

    url = reverse('tasks:tasks_delete', kwargs={'pk': test_task.pk})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Task.objects.count() == 0  # задача удалена


@pytest.mark.django_db
def test_api_without_auth(api_client, test_task):
    url = reverse('tasks:tasks_delete', kwargs={'pk': test_task.pk})
    response = api_client.delete(url)

    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test_jwt_login(api_client, test_user):
    # Получаем токен
    url = reverse('tasks:token_obtain_pair')
    response = api_client.post(url, {
        'username': 'testuser',
        'password': '12345'
    }, format='json')

    assert response.status_code == 200
    assert 'access' in response.data

    access_token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    task_url = reverse('tasks:tasks_list')
    task_response = api_client.get(task_url)
    assert task_response.status_code == 200