from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^(?P<id>\d+)/$', views.post_details, name='post_details'),
]