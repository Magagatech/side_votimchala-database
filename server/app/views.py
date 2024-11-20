from rest_framework import viewsets
from .models import Roles, Student, Election, Position, Candidate, Vote
from .serializers import (
    RolesSerializer, StudentSerializer, ElectionSerializer, PositionSerializer, CandidateSerializer, VoteSerializer
)


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ElectionViewSet(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
