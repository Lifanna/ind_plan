from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .._forms import org_method_work_forms as forms
from .._models import org_method_work_models as models
from django.urls import reverse_lazy
from ind_plan_app import settings
from django.utils.http import (
    url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils import timezone
from django.utils.translation import gettext as _
from django.db import models as django_db_models


@method_decorator(login_required, name='dispatch')
class OrgMethodWorkView(ListView):
    model = models.OrgMethodWork
    paginate_by =  1
    template_name = 'edu_work/org_method_work/index.html'
    context_object_name = "org_method_works"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org_method_work_types'] = models.OrgMethodWorkType.objects.all()

        if self.request.user.status.name == "Преподаватель":
            context['org_method_works'] = self.model.objects.filter(user=self.request.user.id)
            context['totals'] = self.model.objects.filter(
                user=self.request.user.id)\
            .aggregate(
                hours_1_sum=django_db_models.Sum('hours_1'),
            )
        else:
            context['org_method_works'] = self.model.objects.all()
            context['totals'] = self.model.objects.all()\
            .aggregate(
                hours_1_sum=django_db_models.Sum('hours_1'),
            )

        context['fields'] = [_(field.verbose_name) for field in self.model._meta.get_fields() if field.name != "id"]

        return context


@method_decorator(login_required, name='dispatch')
class CreateOrgMethodWorkView(CreateView):
    form_class = forms.OrgMethodWorkForm
    model = models.OrgMethodWork
    template_name = 'edu_work/org_method_work/create.html'
    success_url = reverse_lazy('org_method_work_index')

    # def get_form(self, *args, **kwargs):
    #     form = super(CreateOrgMethodWorkView, self).get_form(*args, **kwargs)
        
    #     return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super(CreateOrgMethodWorkView, self).form_valid(form)

        return response


@method_decorator(login_required, name='dispatch')
class UpdateOrgMethodWorkView(UpdateView):
    form_class = forms.OrgMethodWorkForm
    model = models.OrgMethodWork
    template_name = 'edu_work/org_method_work/update.html'
    success_url = reverse_lazy('org_work_index')


# Обработка не существующих страниц и ошибок
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
