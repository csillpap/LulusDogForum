from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from views import paypal_return, paypal_cancel

urlpatterns = [
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_return),
    url(r'^paypal-cancel', paypal_cancel),

]