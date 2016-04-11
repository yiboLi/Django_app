from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), #use class in views
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), #use class in views
    #The DetailView generic view expects the primary key value captured from the URL to be called "pk"
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), #use class in views
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]