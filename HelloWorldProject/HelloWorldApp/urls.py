from django.conf.urls import url
from HelloWorldApp import views

urlpatterns=[
        url(r'^$',views.index,name='index'),
        ]
