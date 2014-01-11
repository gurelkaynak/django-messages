from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView

from django_messages.views import *

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='inbox/')),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\+\w]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\w]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\w]+)/$', view, name='messages_detail'),
    url(r'^delete/(?P<message_id>[\w]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\w]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
)
