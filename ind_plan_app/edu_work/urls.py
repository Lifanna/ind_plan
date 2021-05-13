# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from ._views import edu_work_views, edu_method_work_views, org_method_work_views, extracurricular_work_views


urlpatterns = [
    # edu_work_views
    path('index/', edu_work_views.EduWorkView.as_view(), name='edu_work_index'),
    path('create/', edu_work_views.CreateEduWorkView.as_view(), name='edu_work_create'),
    path('update/<int:pk>/', edu_work_views.UpdateEduWorkView.as_view(), name='edu_work_update'),
    
    # edu_method_work_views
    path('methodical/create/', edu_method_work_views.CreateEduMethodWorkView.as_view(), name='edu_method_work_create'),
    path('methodical/index/', edu_method_work_views.EduMethodWorkView.as_view(), name='edu_method_work_index'),
    path('methodical/update/<int:pk>/', edu_method_work_views.UpdateEduMethodWorkView.as_view(), name='edu_method_work_update'),
    
    # scientific_work_views
    path('scientific/create/', edu_method_work_views.CreateEduMethodWorkView.as_view(), name='edu_method_work_create'),
    path('scientific/index/', edu_method_work_views.EduMethodWorkView.as_view(), name='edu_method_work_index'),
    path('scientific/update/<int:pk>/', edu_method_work_views.UpdateEduMethodWorkView.as_view(), name='edu_method_work_update'),
    
    # organizational_work_views
    path('organizational/create/', org_method_work_views.CreateOrgMethodWorkView.as_view(), name='org_method_work_create'),
    path('organizational/index/', org_method_work_views.OrgMethodWorkView.as_view(), name='org_method_work_index'),
    path('organizational/update/<int:pk>/', org_method_work_views.UpdateOrgMethodWorkView.as_view(), name='org_method_work_update'),
    
    # extracurricular_work_views basic
    path('extra/index/', extracurricular_work_views.ExtracurricularWorkView.as_view(), name='extracurricular_work_index'),
    
    # extracurricular_work_views Internaional cooperation
    path('extra/int_coop/create/', extracurricular_work_views.CreateInternationalCooperationWorkView.as_view(), name='extra_int_coop_work_create'),
    path('extra/int_coop/index/', extracurricular_work_views.InternationalCooperationWorkView.as_view(), name='extra_int_coop_work_index'),
    path('extra/int_coop/update/<int:pk>/', extracurricular_work_views.UpdateInternationalCooperationWorkView.as_view(), name='extra_int_coop_work_update'),
]

# if DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
