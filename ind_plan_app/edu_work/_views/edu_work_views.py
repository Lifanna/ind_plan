from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .._forms import edu_work_forms as forms
from .._models import edu_work_models as models
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
class EduWorkView(ListView):
    model = models.EducationalWork
    paginate_by = 10
    template_name = 'edu_work/index.html'
    context_object_name = "edu_works"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = _("Welcome to my site")
        context['educational_work_types'] = models.EducationalWorkType.objects.all()

        if self.request.user.status.id == 1:
            context['edu_works'] = self.model.objects.filter(user=self.request.user.id)
            context['totals'] = self.model.objects.filter(
                user=self.request.user.id)\
            .aggregate(
                by_plan_1_sum=django_db_models.Sum('by_plan_1'),
                by_fact_1_sum=django_db_models.Sum('by_fact_1'),
                deviation_1_sum=django_db_models.Sum('deviation_1'),
                by_plan_2_sum=django_db_models.Sum('by_plan_2'),
                by_fact_2_sum=django_db_models.Sum('by_fact_2'),
                deviation_2_sum=django_db_models.Sum('deviation_2'),
                by_plan_annual_sum=django_db_models.Sum('by_plan_annual'),
                by_fact_annual_sum=django_db_models.Sum('by_fact_annual'),
                deviation_annual_sum=django_db_models.Sum('deviation_annual'),
            )
        else:
            context['edu_works'] = self.model.objects.all()
            context['totals'] = self.model.objects.all()\
            .aggregate(
                by_plan_1_sum=django_db_models.Sum('by_plan_1'),
                by_fact_1_sum=django_db_models.Sum('by_fact_1'),
                deviation_1_sum=django_db_models.Sum('deviation_1'),
                by_plan_2_sum=django_db_models.Sum('by_plan_2'),
                by_fact_2_sum=django_db_models.Sum('by_fact_2'),
                deviation_2_sum=django_db_models.Sum('deviation_2'),
                by_plan_annual_sum=django_db_models.Sum('by_plan_annual'),
                by_fact_annual_sum=django_db_models.Sum('by_fact_annual'),
                deviation_annual_sum=django_db_models.Sum('deviation_annual'),
            )

        context['fields'] = [_(field.verbose_name) for field in self.model._meta.get_fields() if field.name != "id"]

        return context

    # def get_queryset(self):
    #     user = self.request.user
    #     return self.model.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CreateEduWorkView(CreateView):
    form_class = forms.EducationalWorkForm
    model = models.EducationalWork
    template_name = 'edu_work/create.html'
    success_url = reverse_lazy('edu_work_index')
    
    # def get_success_url(self):
    #     return reverse_lazy('edu_work_index')

    def get_form(self, *args, **kwargs):
        form = super(CreateEduWorkView, self).get_form(*args, **kwargs)
        # print(form.fields)
        # form.fields['education_work_type'].queryset = models.EducationalWorkType.objects.values("name")
        # form.fields['b_a'].queryset = A.objects.filter(a_user=self.request.user) 
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super(CreateEduWorkView, self).form_valid(form)

        return response


@method_decorator(login_required, name='dispatch')
class UpdateEduWorkView(UpdateView):
    form_class = forms.EducationalWorkForm
    model = models.EducationalWork
    template_name = 'edu_work/update.html'
    success_url = reverse_lazy('edu_work_index')


# Обработка не существующих страниц и ошибок
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
