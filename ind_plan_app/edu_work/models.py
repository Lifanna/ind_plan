from django.db import models


class EducationalWorkType(models.Model):
    name = models.CharField("Тип учебной работы", max_length=255, blank=True)

    def __str__(self):
        return self.name


class EducationalWork(models.Model):
    education_work_type = models.ForeignKey(EducationalWorkType, on_delete=models.SET_NULL, verbose_name="Тип учебной работы", null=True)
    
    by_plan_1 = models.IntegerField("План 1 семестр", blank=True)
    
    by_fact_1 = models.IntegerField("Факт 1 семестр", blank=True)
    
    deviation_1 = models.IntegerField("Отклонение 1 семестр", blank=True)
    
    by_plan_2 = models.IntegerField("План 2 семестр", blank=True)
    
    by_fact_2 = models.IntegerField("Факт 2 семестр", blank=True)
    
    deviation_2 = models.IntegerField("Отклонение 2 семестр", blank=True)

    by_plan_annual = models.IntegerField("План за год", blank=True)

    by_fact_annual = models.IntegerField("Факт за год", blank=True)

    deviation_annual = models.IntegerField("Отклонение за год", blank=True)
