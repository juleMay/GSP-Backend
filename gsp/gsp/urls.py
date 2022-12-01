"""gsp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
import crud_tramite.views
import crud_tramitante.views

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('tramites/', crud_tramite.views.tramite_list),
    path('tramites/<int:id>', crud_tramite.views.tramite_detail),
    path('tramitantes/', crud_tramitante.views.tramitante_list),
    path('tramitantes/<int:id>', crud_tramitante.views.tramitante_detail),
]
