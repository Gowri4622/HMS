from rest_framework import serializers
from .models import CustomUser
from master_app.serializer import StudentSerializer


class UserSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'user_role','students']