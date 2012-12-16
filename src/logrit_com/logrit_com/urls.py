from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView

from projects.models import Project

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logrit_com.views.home', name='home'),
    # url(r'^logrit_com/', include('logrit_com.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="home.html")),

    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^projectindex/$', ListView.as_view(
        queryset=Project.objects.order_by('name'),
        context_object_name='projects',
        template_name='html/projects.html')),
)
