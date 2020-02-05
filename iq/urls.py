from django.contrib import admin
from django.conf.urls import url,include
from . import views
app_name='iq'

urlpatterns = [
    
    url(r'^$',views.index),
]