from django.conf.urls import url

from . import views

app_name='events'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$', views.login, {"template_name": "login.html"}, name='login'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    # ex: /events/
    url(r'^events/$', views.events, name='event_list'),
    # ex: /events/add/
    url(r'^events/add/$', views.add, name='add'),
    # ex: /events/<id>/
    url(r'^events/(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /events/<id>/edit/
    url(r'^events/(?P<event_id>[0-9]+)/edit/$', views.edit, name='edit'),

]
