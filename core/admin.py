from django.contrib import admin
from core import models


@admin.register(models.Address)
class Address(admin.ModelAdmin):
    list_display = ('city', 'street', 'house_number',)
    search_fields = ('city',)


@admin.register(models.Professor)
class Professor(admin.ModelAdmin):
    list_display = ('first_name', 'department',)
    search_fields = ('first_name',)


@admin.register(models.University)
class University(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields = ('name',)


@admin.register(models.Department)
class Department(admin.ModelAdmin):
    list_display = ('name', 'staff_count',)
    search_fields = ('name',)

