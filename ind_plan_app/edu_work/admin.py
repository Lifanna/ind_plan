# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db.models import Q
from ._models import edu_work_models

# Register your models here.

@admin.register(edu_work_models.EducationalWork)
class EducationalWorkAdmin(ModelAdmin):
    """Регистрация модели Учебная работа в админ панели"""

    fieldsets = (
        (None, {'fields': (
            'user',
            'education_work_type',
            'by_plan_1',
            'by_fact_1',
            'deviation_1',
            'by_plan_2',
            'by_fact_2',
            'deviation_2',
            'by_plan_annual',
            'by_fact_annual',
            'deviation_annual',
        )}),
    )
    readonly_fields = (
        # 'user',
        'deviation_1',
        'deviation_2',
        'by_plan_annual',
        'by_fact_annual',
        'deviation_annual',
    )
    # list_display = ('__str__', 'email',)
    list_filter = ('user', 'education_work_type',)
    search_fields = ('user', 'education_work_type',)
    ordering = ('user', 'education_work_type',)
    # inlines = [StudentInline,]

