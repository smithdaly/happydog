from django.conf.urls import url
from . import views
from .venu_actions import *
from .customer_view import *

from .dashboard_view import *
from .dog_view import *

app_name = 'dashboard'
urlpatterns = [
  url(r'^$', dashboardView.as_view(), name='dashboard.index'),
  url(r'^dog/$', dogView.as_view(), name='dog.index'),
	url(r'^dog/getdata/', getData.as_view(), name='dashboard.getdata'),
	url(r'^dog/save/$', dogUpdateView.as_view(), name='dog_save'),
	url(r'^dog/delete/(?P<pk>\d+)/$', dogDeleteView.as_view(), name='dog_delete'),

  url(r'^venu/save/', VenuUpdateView.as_view(), name='venu_save'),
	url(r'^venu/delete/(?P<pk>\d+)/$', VenuDeleteView.as_view(), name='venu_delete'),
	url(r'^customer/$', CustomerView.as_view(), name='customer.index'),
	url(r'^customer/save/$', CustomerUpdateView.as_view(), name='customer_save'),
	url(r'^customer/delete/(?P<pk>\d+)/$', CustomerDeleteView.as_view(), name='customer_delete'),
]
