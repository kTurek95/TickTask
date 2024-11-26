from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # dzięki temu ustawieniu nikt nie będzie wiedział jakie jest hasło

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title', 
            'description',
            'created_at',
            'created_by', 
            'updated_at', 
            'updated_by',
            'deadline', 
            'completed_by', 
            'completed'
            ]
        extra_kwargs = {'created_by': {'read_only':True}}