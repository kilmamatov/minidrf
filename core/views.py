from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from core import serializers
from core import models
from core import filters


class AddressViewSet(ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class ProfessorViewSet(ModelViewSet):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProfessorFilter


class UniversityViewSet(ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


