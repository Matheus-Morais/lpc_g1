"""lpc_g1 URL Configuration

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
from ProvaG1.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', inicio, name='inicio'),
    url(r'^recursos/', Recursos),
    url(r'^eventos/', Eventos),
    url(r'^pessoas/', Pessoas),
    url(r'^artigos/', Artigos),
    url(r'^evento/([0-9]{1})/', EventoX),
    url(r'^pessoa/([0-9]{1})/', PessoaX),
    url(r'^artigo/([0-9]{1})/', ArtigoX),
]
