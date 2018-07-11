from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<projectname_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<projectname_id>[0-9]+)/(?P<jobinformation_id>[0-9]+)/$', views.jobdetail, name='job_detail'),
    url(r'^useradmin/$', views.useradmin, name='detail_job'),
    url(r'^author/(?P<pk>\d+)/edit/$', views.post_edit, name='jenkinsjobsinformation_edit'),
    ]
