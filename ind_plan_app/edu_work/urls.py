# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views as edu_work_views


urlpatterns = [
    path('index/', edu_work_views.EduWorkView.as_view(), name='edu_work_index'),
    path('create/', edu_work_views.CreateEduWorkView.as_view(), name='edu_work_create'),
    path('update/<int:pk>/', edu_work_views.UpdateEduWorkView.as_view(), name='edu_work_update'),
    # path('login/', main_views.CustomLoginView.as_view(template_name='login.html'), name='login'),
]

# if DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

handler404 = 'edu_work.views.handler404'
handler500 = 'edu_work.views.handler500'
