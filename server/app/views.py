from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets


from .models import Student
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = UserSerializer
