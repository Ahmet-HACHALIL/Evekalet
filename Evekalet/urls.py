"""Evekalet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('contactUs/', views.contactUs, name = 'contactUs'),
    path('websiteInfo/', views.websiteInfo, name = 'websiteInfo'),
    path('home/', include('home.urls')),
    path('university/', include('university.urls')),
    path('pdf/', include('pdf_convert.urls')),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view,name = 'logout_view'),
    path('login/', views.login_view,name = 'login_view'),
    path('signup/', views.signup_view,name = 'signup_view'),
    path('agency/', views.agency,name = 'agency'),
    path('loginType/', views.loginType,name = 'loginType'),
    #path('create_student/', views.create_student,name = 'create_student'),
    #path('search/', views.box_search, name='box_search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
