from django.conf.urls import url
from computers import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^computer/$', views.computer, name='computer'),
    url(r'^com_modify/$', views.com_modify, name='modify'),
]
