from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^upload_successful/$', views.upload_successful, name='upload_successful'),
    url(r'^input_job_description/$', views.input_job_description, name='input_job_description'),
    url(r'^job_success/$', views.job_success, name='job_success'),
    url(r'^get_job_descriptions/$', views.get_job_descriptions, name='get_job_descriptions'),
    url(r'^job_list/$', views.job_list, name='job_list'),
    url(r'^job_match/$', views.job_match, name='job_match'),
    url(r'^job_list/(?P<pk>[0-9]+)/edit/$', views.edit_job_description, name='edit_job_description'),
    url(r'^get_cvs/$', views.get_cvs, name='get_cvs'),
]
