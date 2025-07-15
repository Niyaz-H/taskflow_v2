from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend

class IndexView(TemplateView):
    template_name = 'tasks/index.html'

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('user-create', request=request, format=format),
        'tasks': reverse('task-list-create', request=request, format=format)
    })

class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
