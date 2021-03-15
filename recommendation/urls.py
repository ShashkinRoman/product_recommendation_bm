from django.conf.urls import url
from django.urls import path
from recommendation.views import product_recommendation, start_page

urlpatterns = [
    # url('', start_page),
    url(r'^start/(?P<pk>\d+)/$', start_page),
]
