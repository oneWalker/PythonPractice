"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import path,include # 从 django.urls 引入 include
from . import views

urlpatterns = [
    #path(route, view, kwargs=None, name=None)
    #path('admin/', admin.site.urls),
    url(r'^$', views.hello),#和代码path('hello/', admin.site.urls)是类似的
    path('runoob/', views.runoob),
    #进行路由分发，然后统一将路径分发给相应的app，再在自己各自的app里面进行相关的使用
    # path("app01/", include("app01.urls")),
    # path("app02/", include("app02.urls")),
]
