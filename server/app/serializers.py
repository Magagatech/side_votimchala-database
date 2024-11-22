from rest_framework import serializers
from .models import Roles, Student, Election, Position, Candidate, Vote


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    role = RolesSerializer()  # Nested representation of role

    class Meta:
        model = Student
        fields = '__all__'


class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ['id', 'end_date', 'start_date']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'id',
            'election',
            'student',
            'position',
            'manifesto',
            'status',
        ]
        depth = 1  # Includes related FK data


class VoteSerializer(serializers.ModelSerializer):
    voter = StudentSerializer()
    candidate = CandidateSerializer()

    class Meta:
        model = Vote
        fields = '__all__'
