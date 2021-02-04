#-*- codeing = utf-8 -*-
#@Time : 2021/2/1  17:22
#@Aythor : LHW 
#@File : urls.py
#@Software: PyCharm
from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^$', views.index_view)
]