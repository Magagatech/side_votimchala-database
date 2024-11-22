from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Roles, Student, Election, Position, Candidate, Vote,Post
from .serializers import (
    RolesSerializer, StudentSerializer, ElectionSerializer, PositionSerializer, CandidateSerializer, VoteSerializer,PostSerializer
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


class ElectionView(APIView):
    def get(self, request):
        # Retrieve the latest election (or filter as necessary)
        election = Election.objects.last()
        if election:
            serializer = ElectionSerializer(election)
            return Response(serializer.data)
        return Response({"error": "No election found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ElectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
