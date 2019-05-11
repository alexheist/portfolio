from django.conf.urls import (
	url, re_path, include,
)

urlpatterns = [
	re_path('(?P<version>(v1))/contact/', include('website.contact.urls')),
]
