from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import twilio_mgr.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', twilio_mgr.views.index, name='index'),
    # url(r'^db', twilio_mgr.views.db, name='db'),
    path('admin/', admin.site.urls),
]
