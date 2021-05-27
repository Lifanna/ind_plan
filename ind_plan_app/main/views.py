from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
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


class CustomLogoutView(LoginView):
    """Custom login view"""
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    next_page = None
    template_name = 'login.html'
    extra_context = None

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):
        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            next_page = resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            next_page = self.next_page

        if (self.redirect_field_name in self.request.POST or
                self.redirect_field_name in self.request.GET):
            next_page = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            'site': current_site,
            'site_name': current_site.name,
            'title': _('Logged out'),
            **(self.extra_context or {})
        })
        return context


    def logout_then_login(request, login_url=None):
        """
        Log out the user if they are logged in. Then redirect to the login page.
        """
        login_url = resolve_url(login_url or settings.LOGIN_URL)
        return LogoutView.as_view(next_page=login_url)(request)


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    def get_template_names(self):
        template_name = ['main/index.html']

        if self.request.user.status.name == 'Преподаватель':
            template_name = ['main/index.html']
        elif self.request.user.status.name == 'Заведующий кафедрой':
            template_name = ['main/index.html']

        return template_name

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
    print("DDDDDD")
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
