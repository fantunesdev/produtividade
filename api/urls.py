from django.urls import path, include

from api.views.area_views import *
from api.views.atividade_views import *
from api.views.pessoa_views import PessoaArea
from api.views.plataforma_views import *
from api.views.subarea_views import *

urlpatterns = [
    path('atividades/', AtividadesList.as_view(), name='atividades-list'),
    path('areas/', AreaList.as_view(), name='areas-list'),
    path('areas/<int:area_id>/', AreaDetalhes.as_view(), name='area-detalhes'),
    path('areas/<int:area_id>/subareas/', SubAreaArea.as_view(), name='area_subareas-detalhes'),
    path('areas/<int:area_id>/plataformas/', PlataformaArea.as_view(), name='plataforma-area'),
    path('areas/<int:area_id>/pessoas/', PessoaArea.as_view(), name='pessoa-area'),

    path('subareas/', SubAreaList.as_view(), name='subarea-list'),
    path('subareas/<int:subarea_id>/', SubAreaDetalhes.as_view(), name='subarea-detalhes')
]
