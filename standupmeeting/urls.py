from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^$', 'home.views.home_login', name='home_login'),
    url(r'^admin/', include(admin.site.urls)),
]

#Dashboard
urlpatterns += [
	url(r'^dashboard/', include('dashboard.urls')),
]