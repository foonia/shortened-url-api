from django.urls import re_path
from . import views

urlpatterns = [ 
    re_path(r'^short/(?P<url>.+)/$', views.ShortenedUrlAPIView.as_view(), 
        name='shortened_url'),
]
