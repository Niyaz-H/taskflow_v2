from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'Test Task'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        Task.objects.create(user=self.user, title='Test Task 1')
        Task.objects.create(user=self.user, title='Test Task 2')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_update_task(self):
        task = Task.objects.create(user=self.user, title='Test Task')
        response = self.client.put(f'/api/tasks/{task.id}/', {'title': 'Updated Task'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.get().title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(user=self.user, title='Test Task')
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)

    def test_filter_tasks_by_completed(self):
        Task.objects.create(user=self.user, title='Completed Task', completed=True)
        Task.objects.create(user=self.user, title='Incomplete Task', completed=False)
        response = self.client.get('/api/tasks/?completed=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Completed Task')

    def test_filter_tasks_by_priority(self):
        Task.objects.create(user=self.user, title='High Priority Task', priority='H')
        Task.objects.create(user=self.user, title='Low Priority Task', priority='L')
        response = self.client.get('/api/tasks/?priority=H')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'High Priority Task')
