"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
	#主页
    url(r'^$', views.view,name='view'),

    #显示转派详情
    url(r'^/(?P<topic_id>\d+)/$',views.information,name='information'),

    #用于添加工单的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),

    #用于修改工单的网页
    url(r'^edit_topic/(?P<topic_id>\d+)/$',views.edit_topic,name='edit_topic'),

    #用于转派工单
    url(r'^forward_topic/(?P<topic_id>\d+)/$',views.forward_topic,name='forward_topic'),

    #用于反馈
    url(r'^forward_topic1/(?P<topic_id>\d+)/$',views.forward_topic1,name='forward_topic1'),

    #用于删除
    url(r'^del_topic/(?P<topic_id>\d+)/$',views.del_topic,name='del_topic'),

    #用于完成
    url(r'^finished_topic/(?P<topic_id>\d+)/$',views.finished_topic,name='finished_topic'),

]
