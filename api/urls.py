from django.urls import path
from .views import *


urlpatterns = [
    path('atividades', AtividadesList.as_view(), name='atividades-list')
]