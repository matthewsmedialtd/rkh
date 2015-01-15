from django.conf.urls import patterns, include, url
from django.contrib import admin

from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
    # ex: /polls/5/
    url(r'^polls/(?P<question_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^polls/(?P<question_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),	
    url(r'^admin/', include(admin.site.urls)),
)
