from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, TaskViewSet

# Define a router for the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# URL patterns for the tasks app
urlpatterns = [
    path('', index, name='index'),  # This will render the HTML UI
    path('api/', include(router.urls)),  # This handles all the API endpoints
]