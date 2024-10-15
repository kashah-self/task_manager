# tasks/tests.py
from django.test import TestCase
from tasks.models import Task
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class TaskModelTestCase(TestCase):
    """Test suite for the Task model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.task_title = "Test Task"
        self.task_description = "Test Task Description"
        self.task_status = "Pending"
        self.task = Task(title=self.task_title, description=self.task_description, status=self.task_status)

    def test_model_can_create_a_task(self):
        """Test if a Task object can be created."""
        old_count = Task.objects.count()
        self.task.save()
        new_count = Task.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_string_representation(self):
        """Test the string representation of the Task model."""
        self.assertEqual(str(self.task), self.task.title)

class TaskAPITestCase(TestCase):
    """Test suite for the API views."""

    def setUp(self):
        """Define the test client and initialize test data."""
        self.client = APIClient()
        self.task_data = {
            'title': 'Test API Task',
            'description': 'Test API Task Description',
            'status': 'Pending'
        }
        self.task = Task.objects.create(**self.task_data)

    def test_api_can_create_a_task(self):
        """Test the API has task creation capability."""
        response = self.client.post(reverse('task-list'), self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_task(self):
        """Test the API can retrieve a task."""
        task = Task.objects.get()
        response = self.client.get(reverse('task-detail', kwargs={'pk': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, task.title)

    def test_api_can_update_a_task(self):
        """Test the API can update a task."""
        task = Task.objects.get()
        updated_task_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Task Description',
            'status': 'Completed'
        }
        response = self.client.put(reverse('task-detail', kwargs={'pk': task.id}), updated_task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task Title')

    def test_api_can_delete_a_task(self):
        """Test the API can delete a task."""
        task = Task.objects.get()
        response = self.client.delete(reverse('task-detail', kwargs={'pk': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)