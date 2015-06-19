from django.conf.urls import include, url,patterns
from django.contrib import admin
admin.autodiscover()

import ada.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ada.views.index, name='index'),
    
    url(r'^admin/', include(admin.site.urls)),

)
