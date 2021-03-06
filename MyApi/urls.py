"""MyApi URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # rest_framework 사용을 위한 url
    path('rest-auth/', include('rest_auth.urls')), # user-auth 기능을 위해 추가: login, logout 비밀번호 변경
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('customUser/', include('customUser.api.urls')), # 프로젝트에서 앱으로 url 연결
]