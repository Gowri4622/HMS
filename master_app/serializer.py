from rest_framework import serializers
from .models import Student, Hostel, Room, Warden, Parent, HostelFees
from django.contrib.auth import get_user_model
import string
import random


class StudentSerializer(serializers.ModelSerializer):
    # date_of_birth = serializers.DateField(format="%Y-%m-%d")
    check_in_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','register_number', 'gender','date_of_birth','contact_number', 'email', 'parents_number', 'blood_group', 'department', 'check_in_date','hostel','owner']

    def create(self, validated_data):
        first_name = validated_data['register_number']
        username = first_name

        def generate_password():
            length = 8
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(characters) for i in range(length))
        
        password = generate_password()

        user_data = {
            'username': username,
            'password': password,
            'user_role': 'Student',  
        }

        print(username)
        print(password)
        user = get_user_model().objects.create(**user_data)

        user.set_password(password)
        user.save()

        validated_data['owner'] = user
        student = Student.objects.create(**validated_data)

        return student
    


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['hostel_name', 'hostel_type', 'location', 'number_of_floors', 'number_of_rooms', 'type_of_room', 'warden_assigned']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_strength', 'room_assets']


class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = ['register_number','first_name', 'last_name', 'gender', 'date_of_birth', 'qualification', 'contact_number', 'email','hostel']

    def create(self, validated_data):
        first_name = validated_data['register_number']
        username = first_name.lower()

        def generate_password():
            length = 8
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(characters) for i in range(length))
        
        password = generate_password()

        user_data = {
            'username': username,
            'password': password,
            'user_role': 'Warden',  
        }

        print(username)
        print(password)
        user = get_user_model().objects.create(**user_data)

        user.set_password(password)
        user.save()

        validated_data['owner'] = user
        warden = Warden.objects.create(**validated_data)

        return warden



class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'student_name', 'contact_number', 'email']



class HostelFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelFees
        fields = ['rent', 'food', 'transport']



