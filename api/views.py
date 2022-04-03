from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import TodoSerializer
from todo.models import Todo


# Create your views here.


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')