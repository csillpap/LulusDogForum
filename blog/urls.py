from django.conf.urls import url
from views import post_list, post_detail


urlpatterns = [
    url(r'^blogposts$', post_list, name='blogposts'),
    url(r'^(?P<id>\d+)$', post_detail),
]