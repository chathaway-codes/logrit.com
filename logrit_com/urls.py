from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Zinnia URLs... I don't want a bunch of stuff
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^search/', include('zinnia.urls.search')),


    url(r'^weblog/', include('zinnia.urls.entries')),
    url(r'^weblog/', include('zinnia.urls.archives')),
    url(r'^weblog/', include('zinnia.urls.shortlink')),
    url(r'^weblog/', include('zinnia.urls.quick_entry')),
    url(r'^weblog/feeds/', include('zinnia.urls.feeds')),
    url(r'^weblog/authors/', include('zinnia.urls.authors')),
    url(r'^weblog/categories/', include('zinnia.urls.categories')),
    url(r'^weblog/tags/', include('zinnia.urls.tags')),


    url(r'^', include('cms.urls')),


    # TemplateView + Login
    #url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), {}, 'home'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
