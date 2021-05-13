from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .._forms import edu_method_work_forms as forms
from .._models import edu_method_work_models as models
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
class EduMethodWorkView(ListView):
    model = models.EduMethodWork
    paginate_by =  1
    template_name = 'edu_work/edu_method_work/index.html'
    context_object_name = "edu_method_works"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = _("Welcome to my site")

        if self.request.user.status.name == "Преподаватель":
            context['edu_works'] = self.model.objects.filter(user=self.request.user.id)
            context['totals'] = self.model.objects.filter(
                user=self.request.user.id)\
            .aggregate(
                hours_1_sum=django_db_models.Sum('hours_1'),
                by_plan_sum=django_db_models.Sum('by_plan'),
                by_fact_sum=django_db_models.Sum('by_fact'),
            )
        else:
            context['edu_works'] = self.model.objects.all()
            context['totals'] = self.model.objects.all()\
            .aggregate(
                hours_1_sum=django_db_models.Sum('hours_1'),
                by_plan_sum=django_db_models.Sum('by_plan'),
                by_fact_sum=django_db_models.Sum('by_fact'),
            )

        context['fields'] = [_(field.verbose_name) for field in self.model._meta.get_fields() if field.name != "id"]

        return context



@method_decorator(login_required, name='dispatch')
class CreateEduMethodWorkView(CreateView):
    form_class = forms.EduMethodWorkForm
    model = models.EduMethodWork
    template_name = 'edu_work/edu_method_work/create.html'
    success_url = reverse_lazy('edu_method_work_index')

    def get_form(self, *args, **kwargs):
        form = super(CreateEduMethodWorkView, self).get_form(*args, **kwargs)
        # print(form.fields)
        # form.fields['education_work_type'].queryset = models.EducationalWorkType.objects.values("name")
        # form.fields['b_a'].queryset = A.objects.filter(a_user=self.request.user) 
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super(CreateEduMethodWorkView, self).form_valid(form)

        return response


@method_decorator(login_required, name='dispatch')
class UpdateEduMethodWorkView(UpdateView):
    form_class = forms.EduMethodWorkForm
    model = models.EduMethodWork
    template_name = 'edu_work/edu_method_work/update.html'
    success_url = reverse_lazy('edu_method_work_index')


# Обработка не существующих страниц и ошибок
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
