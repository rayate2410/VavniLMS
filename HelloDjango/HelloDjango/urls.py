from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #(r'^hello_world/$', 'HelloDjango.views.index'),
    (r'^$',"HelloDjango.views.index"),
    (r'^applyForLeave.psp$',"HelloDjango.views.apply_for_leave"),
)