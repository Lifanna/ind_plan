from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from . import forms
from . import models
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


# @method_decorator(login_required, name='dispatch')
class EduWorkView(ListView):
    model = models.EducationalWork
    paginate_by =  1
    template_name = 'edu_work/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = _("Welcome to my site")
        context['fields'] = [field.name for field in self.model._meta.get_fields()]

        return context


# @method_decorator(login_required, name='dispatch')
class CreateEduWorkView(CreateView):
    form_class = forms.EducationalWorkForm
    model = models.EducationalWork
    template_name = 'edu_work/create.html'
    
    def get_success_url(self):
        return reverse_lazy('edu_work_index')

    def get_form(self, *args, **kwargs):
        form = super(CreateEduWorkView, self).get_form(*args, **kwargs)
        # print(form.fields)
        # form.fields['education_work_type'].queryset = models.EducationalWorkType.objects.values("name")
        # form.fields['b_a'].queryset = A.objects.filter(a_user=self.request.user) 
        return form


# @method_decorator(login_required, name='dispatch')
class UpdateEduWorkView(UpdateView):
    model = models.EducationalWork
    template_name = 'edu_work/update.html'


# Обработка не существующих страниц и ошибок
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
