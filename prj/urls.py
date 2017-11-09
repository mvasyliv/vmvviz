from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.prj_list, name='prj_list'),
    url(r'^prj/(?P<pk>[0-9]+)/$', views.prj_detail, name='prj_detail'),
]
