from django.conf.urls import patterns, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', 'dashboard_home', name='dashboard_home'),
    url(r'^configure/$', 'configure', name='configure'),
    url(r'^compose/$', 'compose', name='compose'),
    url(r'^log/$', 'log', name='log'),
     url(r'^monthly-summary/$', 'monthly_summary', name='monthly_summary'),
    )