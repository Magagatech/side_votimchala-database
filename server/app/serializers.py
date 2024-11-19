from rest_framework import serializers
from cryptography.fernet import Fernet
from .models import Student
from django.conf import settings


# secret_key = settings.SECRET_ENCRYPTION_KEY
# cipher_suite = Fernet(secret_key)
# print(secret_key)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # def to_representation(self, instance):
        # data = super().to_representation(instance)

        # data['firstname'] = cipher_suite.encrypt(
        #     data['firstname'].encode()).decode()
        # data['lastname'] = cipher_suite.encrypt(
        #     data['lastname'].encode()).decode()

        # return data
