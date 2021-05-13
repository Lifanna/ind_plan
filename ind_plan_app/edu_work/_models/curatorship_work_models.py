from django.db import models
from main import models as main_models
from django.utils.translation import ugettext_lazy as _


class CuratorshipWorkType(models.Model):
    name = models.CharField(_("Curatorship work type"), max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Curatorship work type')
        verbose_name_plural = _('Curatorship work types')


class CuratorshipWork(models.Model):
    cur_work_type = models.ForeignKey(CuratorshipWorkType, on_delete=models.SET_NULL, 
        verbose_name=_("Curatorship work type"), null=True)

    date = models.DateField("Date of execution")

    document = models.FileField("Supporting document", upload_to='uploads/')

    user = models.ForeignKey(main_models.User, on_delete=models.SET_NULL, verbose_name=_("Author"), null=True)

    class Meta:
        verbose_name = _('Curatorship work')
        verbose_name_plural = _('Curatorship works')
