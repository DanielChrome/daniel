from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
	url(r"^$","postagens.views.home", name="home"),
	url(r"^index/$","postagens.views.home", name="home"),
    # url(r"^$", direct_to_template, {
    url(r"^admin/", include(admin.site.urls)),
    url(r"^blog/$","postagens.views.blog", name="blog"),
    url(r"^portfolio/$","postagens.views.portifolio", name="portifolio"),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
