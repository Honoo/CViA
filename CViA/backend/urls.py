from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^upload_successful/$', views.upload_successful, name='upload_successful'),
    url(r'^input_job_description/$', views.input_job_description, name='input_job_description'),
    url(r'^job_success/$', views.job_success, name='job_success'),
]