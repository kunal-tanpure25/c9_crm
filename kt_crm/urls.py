"""
URL configuration for kt_crm project.

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
from django.contrib import admin
from django.urls import path , include

from c9.views import index
from c9.views import about
from userprofile.views import signup
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('dashboard/',include('dashboard.urls')),
    path('log-in/',views.LoginView.as_view(template_name = 'userprofile/login.html'),name = 'login'),
    path('sign-up',signup , name='signup'),
    path('log-out/',views.LogoutView.as_view() , name = 'logout'),

]
