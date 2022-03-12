"""produtividade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from login.views import logar_usuario, deslogar_usuario
from atividades.views.atividade_views import listar_semana_atual

urlpatterns = [
    path('', listar_semana_atual),

    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('atividades/', include('atividades.urls.atividade_urls')),
    path('atividades/areas/', include('atividades.urls.area_urls')),
    path('atividades/sub_areas/', include('atividades.urls.sub_area_urls')),
    path('atividades/plataformas/', include('atividades.urls.plataforma_urls')),

    path('usuarios/', include('login.urls')),
    path('login/', logar_usuario, name='logar_usuario'),
    path('logout/', deslogar_usuario, name='deslogar_usuario'),
]
