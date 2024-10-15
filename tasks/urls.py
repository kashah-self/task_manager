from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, TaskViewSet

# Defining a router for the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# URL patterns for the tasks app
urlpatterns = [
    path('', index, name='index'),  # it will render the HTML UI
    path('api/', include(router.urls)),  # it handles all the API endpoints
]