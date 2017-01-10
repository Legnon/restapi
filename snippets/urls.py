from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
	url(r'^$', views.api_root),
	url(r'^list/$', views.SnippetList.as_view(), name='snippet-list'),
	url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
	url(r'^(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

	url(r'^users/$', views.UserList.as_view(), name='user-list'),
	url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
