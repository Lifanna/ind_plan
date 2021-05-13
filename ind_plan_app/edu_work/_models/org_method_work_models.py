from django.db import models
from main import models as main_models
from django.utils.translation import ugettext_lazy as _
from ..validators.validators import validate_file_extension, upload_to
import os


class OrgMethodWorkType(models.Model):
    name = models.CharField(_("Organizational methodical work type"), max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Organizational methodical work type')
        verbose_name_plural = _('Organizational methodical work types')


class OrgMethodWork(models.Model):
    org_method_work_type = models.ForeignKey(OrgMethodWorkType, on_delete=models.SET_NULL, 
        verbose_name=_("Organizational methodical work type"), null=True)

    information_name = models.TextField(_("Prepared information name"), blank=True)

    hours_1 = models.IntegerField(_("Hours count"), blank=True)

    execution_period = models.DateField("Period of execution")

    document = models.FileField("Supporting document", upload_to=upload_to, validators=[validate_file_extension])

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    class Meta:
        verbose_name = _('Organizational methodical work')
        verbose_name_plural = _('Organizational methodical works')
