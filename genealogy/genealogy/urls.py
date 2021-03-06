"""genealogy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from genealogy_app.views import LoginView, mainPage, CreateAccount, AnceatorView, AddAnceator

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/?$', LoginView.as_view(), name='login-form'),
    url(r'^main/?$', mainPage.as_view(), name='main-form'),
    url(r'^newuser/?$', CreateAccount.as_view(), name='new_user-form'),
    url(r'^anceators/?$', AnceatorView.as_view(),name='anceator-list'),
    url(r'^add/?$', AddAnceator.as_view(),name='anceator-form'),

    

]
