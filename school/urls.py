"""school URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from biblioteca.views import register, register_autor, inicio, auth_view, listar_autor

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register),
    url(r'^register_autor/$', register_autor),
    url(r'^autores/$', listar_autor),
    url(r'^auth_view/$', auth_view),
    url(r'^$', inicio),
    url(r'^home/$', 'biblioteca.views.home'),
    url(r'^register_user/$', 'biblioteca.views.register_user'),
    url(r'^register_success/$', 'biblioteca.views.register_success'),
    url(r'^buscar/autor/$', 'biblioteca.views.buscar_autor'),
    url(r'^logout/$', 'biblioteca.views.cerrar'),
    url(r'^delete/autor/(?P<id>\d+)', 'biblioteca.views.delete_autor'),
    url(r'^update/autor/(?P<id>\d+)', 'biblioteca.views.updateAutor'),


]
