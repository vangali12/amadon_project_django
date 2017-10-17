from django.conf.urls import url
from django.contrib import admin

from . import views

def test(request):
	print """


	app level urls


	"""

urlpatterns = [
	url(r'^amadon$', views.index),
	url(r'^amadon/buy$', views.buy),
	url(r'^amadon/checkout$', views.checkout),
	url(r'^amadon/clear$', views.clear),
]