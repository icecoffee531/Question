"""Graduation_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/login/', Login),
    path('apis/loginout/', Loginout),
    path('apis/index/', Index),
    path('apis/regist/', regist),
    path('apis/answer_detail/', answer_detail),
    path('apis/answer/', answer),
    path('apis/change_password/', change_password),
    path('apis/people/', People),
    path('apis/delete/', Delete),
    path('apis/change/', Change)
]
