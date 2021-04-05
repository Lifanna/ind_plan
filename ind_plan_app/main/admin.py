# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db.models import Q
from . import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('login',)}),
        ('Личная информация', {
            'fields': ('password', 'first_name', 'last_name', 'patronymic',)
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('__str__', 'email',)
    list_filter = ('email', 'login', 'first_name', 'last_name',)
    search_fields = ('email', 'login', 'first_name', 'last_name',)
    ordering = ('login',)
    # inlines = [StudentInline,]

