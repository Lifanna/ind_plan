from django.db import models
from main import models as main_models
from django.utils.translation import ugettext_lazy as _


class Specialty(models.Model):
    name = models.CharField(_("Specialty name"), max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')


class EduMethodWorkType(models.Model):
    name = models.CharField(_("Educational methodical work type"), max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Educational methodical work type')
        verbose_name_plural = _('Educational methodical work types')


class EduMethodWork(models.Model):
    edu_method_work_type = models.ForeignKey(EduMethodWorkType, on_delete=models.SET_NULL, 
        verbose_name=_("Educational methodical work type"), null=True)

    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, verbose_name=_("Specialty"), null=True)

    hours_1 = models.IntegerField(_("Hours count"), blank=True)

    by_plan = models.IntegerField(_("Plan"), blank=True)

    by_fact = models.IntegerField(_("Fact"), blank=True)

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    class Meta:
        verbose_name = _('Educational work')
        verbose_name_plural = _('Educational works')
