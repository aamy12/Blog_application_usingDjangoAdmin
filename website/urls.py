from django.conf.urls import url
from . import views
from .feeds import PostsFeed

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,
        name='post_detail_view'),
    url(r'^feed/$', PostsFeed(), name='post_feed'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
