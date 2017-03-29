from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.latest_stories, name='latest_stories'),
    url(r'^top-stories/$', views.top_stories, name='top_stories'),
    url(r'^india/$', views.india, name='india'),
    url(r'^world/$', views.world, name='world'),
    url(r'^business/$', views.business, name='business'),
    url(r'^cricket/$', views.cricket, name='cricket'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^tech/$', views.tech, name='tech'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^auto/$', views.auto, name='auto'),
    # url(r'^(?P<id>\d+)/$', views.post_details, name='post_details'),
]