from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^upload_successful/$', views.upload_successful, name='upload_successful'),
    url(r'^input_job_description/$', views.input_job_description, name='input_job_description'),
    url(r'^job_success/$', views.job_success, name='job_success'),
    url(r'^get_job_descriptions/$', views.get_job_descriptions, name='get_job_descriptions'),
    url(r'^get_matching_cvs/(?P<pk>[0-9]+)/$', views.get_matching_cvs, name='get_matching_cvs'),
    url(r'^job_list/$', views.job_list, name='job_list'),
    url(r'^job_match/(?P<pk>[0-9]+)/$', views.job_match, name='job_match'),
    url(r'^job_list/(?P<pk>[0-9]+)/edit/$', views.edit_job_description, name='edit_job_description'),
    url(r'^get_cvs/$', views.get_cvs, name='get_cvs'),
    url(r'^cv_list/$', views.cv_list, name='cv_list'),
    url(r'^cv_list/(?P<pk>[0-9]+)/edit/$', views.edit_cv, name='edit_cv'),
    url(r'^delete_cv/$', views.delete_cv, name='delete_cv'),
    url(r'^delete_job/$', views.delete_job, name='delete_job'),
]
