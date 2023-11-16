from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateTodoAPIView

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('todos/new_task/', CreateTodoAPIView.as_view(), name='create-a-task'),
]