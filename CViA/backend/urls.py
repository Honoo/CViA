from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_cv/$', views.upload_cv, name='upload_cv'),
]