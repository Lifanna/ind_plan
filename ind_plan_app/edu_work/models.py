from django.db import models


class EducationalWorkType(models.Model):
    name = models.CharField(max_length=255, blank=True)


class EducationalWork(models.Model):
    education_work_type = models.ForeignKey(EducationalWorkType, on_delete=models.SET_NULL, null=True)
    
    by_plan_1 = models.IntegerField("План 1 семестр", on_delete=models.SET_NULL, null=True)
    
    by_fact_1 = models.IntegerField("Факт 1 семестр", on_delete=models.SET_NULL, null=True)
    
    deviation_1 = models.IntegerField("Отклонение 1 семестр", on_delete=models.SET_NULL, null=True)
    
    by_plan_2 = models.IntegerField("План 2 семестр", on_delete=models.SET_NULL, null=True)
    
    by_fact_2 = models.IntegerField("Факт 2 семестр", on_delete=models.SET_NULL, null=True)
    
    deviation_2 = models.IntegerField("Отклонение 2 семестр", on_delete=models.SET_NULL, null=True)

    by_plan_annual = models.IntegerField("План за год", on_delete=models.SET_NULL, null=True)

    by_fact_annual = models.IntegerField("Факт за год", on_delete=models.SET_NULL, null=True)

    deviation_annual = models.IntegerField("Отклонение за год", on_delete=models.SET_NULL, null=True)
