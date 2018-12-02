from django.conf.urls import url, include
from  .  import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name=',login'),
    url(r'^register/$', views.register, name=',register'),
    url(r'^showLoc/$', views.showLoc, name=',showLoc'),
    url(r'^afd/$', views.afd, name=',afd'),
    url(r'^b/$', views.b, name=',b'),
    url(r'^pathway/$', views.pathway, name=',pathway'),
    url(r'^pavilion/$', views.pavilion, name=',pavilion'),
    url(r'^dd/$', views.dd, name=',dd'),
    url(r'^keep/$', views.keep, name=',keep'),
    url(r'^map/$', views.map, name=',map'),
]
