from rest_framework import serializers
from .models import StudentData
class Student_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = ['name', 'department', 'age']
        # exclude = ('name',)

