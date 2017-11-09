from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.prj_list, name='prj_list')
]
