from core import models
import django_filters


class ProfessorFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    middle_name = django_filters.CharFilter(field_name='middle_name', lookup_expr='icontains')

    class Meta:
        model = models.Professor
        fields = ('first_name', 'last_name', 'middle_name')
