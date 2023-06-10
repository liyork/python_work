"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 路由地址(''与基础路由匹配)，要调用view中那个函数，将这个url模式的名称指定为index
    path('', views.index, name='index'),

    # topic
    path('topics/', views.topics, name='topics'),
    # 特定主题
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # create topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # 添加新条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
