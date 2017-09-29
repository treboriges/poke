from django.conf.urls import url
from . import views

def test(request, otherid):
    print """

        Hi

        """
urlpatterns = [
    url(r'^$', views.index),
    url(r'^poke/(?P<otherid>\d+)/$', views.poke)
]
