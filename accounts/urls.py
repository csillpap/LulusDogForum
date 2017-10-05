from django.conf.urls import url
from views import register, profile


urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^profile', profile, name='profile'),
]