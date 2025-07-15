from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_root),
    path('tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
    path('register/', views.UserCreate.as_view(), name='user-create'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]