from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView
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


class CustomLoginView(LoginView):
    """Custom login view"""
    authentication_form = forms.LoginForm
    template_name = 'login.html'


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    def get_template_names(self, request):
        template_name = 'main/index.html'
        if request.user.status.name == 'Преподаватель':
            template_name = 'main/index_tutor.html'
        elif request.user.status.name == 'Заведующий кафедрой':
            template_name = 'main/index_head.html'

        return ['%s.html' % self.kwargs['template']]

    def get_success_url(self):
        return '/registration/student/step2' + '/%d'%self.object.pk


@method_decorator(login_required, name='dispatch')
class UserRegistrationView(CreateView):
    model = models.User
    template_name = 'registration/signup.html'
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def get_success_url(self):
        return '/registration/student/step2' + '/%d'%self.object.pk
    
    def form_valid(self, form):
        user = form.save()
        user.add(self.request.user.id)
        return super(UserRegistrationView, self).form_valid(form)


# Обработка не существующих страниц и ошибок
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
