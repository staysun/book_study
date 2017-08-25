"""book_study URL Configuration

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
from book import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/', views.base),
    url(r'^index/', views.index),
    url(r'^addAuthor/', views.addAuthor),
    url(r'^showAuthor/', views.showAuthor),
    url(r'^addPublisher/', views.addPublisher),
    url(r'^showPublisher/', views.showPublisher),
    url(r'^delAuthor/', views.delAuthor),
    url(r'^delPublisher/', views.delPublisher),
    url(r'^addbook/', views.addbook),

]
