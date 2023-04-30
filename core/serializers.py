from rest_framework import serializers
from core import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'
        read_only_fields = ('staff_count',)


class ProfessorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = models.Professor
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = models.University
        fields = '__all__'
