from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)  # localhost:8000/snippets/snippets/
router.register(r'users', views.UserViewSet)  # localshot:8000/snippets/users/

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]


# snippet_list = SnippetViewSet.as_view({
# 	'get': 'list',
# 	'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
# 	'get': 'retrieve',
# 	'put': 'update',
# 	'patch': 'partial_update',
# 	'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
# 	'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
# 	'get': 'list'
# })
# user_detail = UserViewSet.as_view({
# 	'get': 'retrieve'
# })

# urlpatterns = [
# 	url(r'^$', api_root),
# 	url(r'^list/$', snippet_list, name='snippet-list'),
# 	url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet-detail'),
# 	url(r'^(?P<pk>\d+)/highlight/$', snippet_highlight, name='snippet-highlight'),

# 	url(r'^users/$', user_list, name='user-list'),
# 	url(r'^users/(?P<pk>\d+)/$', user_detail, name='user-detail'),
# ]

# urlpatterns = [
# 	url(r'^$', views.api_root),
# 	url(r'^list/$', views.SnippetList.as_view(), name='snippet-list'),
# 	url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
# 	url(r'^(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

# 	url(r'^users/$', views.UserList.as_view(), name='user-list'),
# 	url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
