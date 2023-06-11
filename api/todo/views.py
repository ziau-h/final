from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.core.cache import cache

class TodoViewset(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer