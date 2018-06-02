from django.urls import re_path
from . import views

urlpatterns = [ 
    re_path(r'^target/(?P<target_url>.+)/$', views.TargetUrlAPIView.as_view(), 
        name='target_url'),
]
