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
    is_active = serializers.BooleanField(
        read_only=True)  # Adding a custom field

    class Meta:
        model = Election
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Nested representation of the student
    position = PositionSerializer()

    class Meta:
        model = Candidate
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    voter = StudentSerializer()
    candidate = CandidateSerializer()

    class Meta:
        model = Vote
        fields = '__all__'
