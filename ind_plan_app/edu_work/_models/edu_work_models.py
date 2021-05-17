from django.db import models
from main import models as main_models
from django.utils.translation import ugettext_lazy as _


class EducationalWorkType(models.Model):
    name = models.CharField(_("Educational work type"), max_length=255, blank=True)

    is_deleted = models.BooleanField(_("Is deleted"), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Educational work type')
        verbose_name_plural = _('Educational work types')


class EducationalWork(models.Model):
    education_work_type = models.ForeignKey(EducationalWorkType, on_delete=models.SET_NULL, verbose_name=_("Educational work type"), null=True)
    
    by_plan_1 = models.IntegerField(_("Plan 1 semester"), blank=True)
    
    by_fact_1 = models.IntegerField(_("Fact 1 semester"), blank=True)
    
    deviation_1 = models.IntegerField(_("Deviation 1 semester"), blank=True)
    
    by_plan_2 = models.IntegerField(_("Plan 2 semester"), blank=True)
    
    by_fact_2 = models.IntegerField(_("Fact 2 semester"), blank=True)
    
    deviation_2 = models.IntegerField(_("Deviation 2 semester"), blank=True)

    by_plan_annual = models.IntegerField(_("Plan annual"), blank=True)

    by_fact_annual = models.IntegerField(_("Fact annual"), blank=True)

    deviation_annual = models.IntegerField(_("Deviation annual"), blank=True)

    approved = models.BooleanField(_("Approval status"), default=False)

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    is_deleted = models.BooleanField(_("Is deleted"), default=False)

    def calculated_fields(self):
        self.deviation_1 = self.by_plan_1 + self.by_fact_1
        self.deviation_2 = self.by_plan_2 + self.by_fact_2

        self.by_plan_annual = self.by_plan_1 + self.by_plan_2
        self.by_fact_annual = self.by_fact_1 + self.by_fact_2
        self.deviation_annual = self.by_plan_annual + self.by_fact_annual

    def save(self, *args, **kwargs):
        self.calculated_fields()

        super(EducationalWork, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Educational work')
        verbose_name_plural = _('Educational works')
