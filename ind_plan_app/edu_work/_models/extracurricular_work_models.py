from django.db import models
from main import models as main_models
from django.utils.translation import ugettext_lazy as _


class InternationalCooperationWorkType(models.Model):
    name = models.CharField(_("Extracurricular work type"), max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('International cooperation work type')
        verbose_name_plural = _('International cooperation work types')


class InternationalCooperationWork(models.Model):
    int_coop_work_type = models.ForeignKey(InternationalCooperationWorkType, on_delete=models.SET_NULL, 
        verbose_name=_("International cooperation work type"), null=True)

    hours_1 = models.IntegerField(_("Hours count"), blank=True)

    start_date = models.DateField(_("Start date"))

    end_date = models.DateField(_("End date"))

    completed = models.BooleanField(_("Completion mark"), blank=True, null=True)

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    class Meta:
        verbose_name = _('International cooperation work')
        verbose_name_plural = _('International cooperation works')


class VocationalGuidanceWork(models.Model):
    fullname = models.IntegerField(_("Fullname"))

    phone = models.DateField(_("Phone number"))

    educational_institution = models.CharField(_("Educational institution"), max_length=255)

    email = models.EmailField("Email", blank=True, null=True)

    parent_contacts = models.CharField(_("Contacts of parents"),  max_length=255, blank=True, null=True)

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    class Meta:
        verbose_name = _('Vocational guidance work')
        verbose_name_plural = _('Vocational guidance works')
