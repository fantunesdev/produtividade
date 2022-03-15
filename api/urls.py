from django.urls import path, include

from api.views.area_views import *
from api.views.atividade_views import *
from api.views.sub_area_views import *

urlpatterns = [
    path('atividades/', AtividadesList.as_view(), name='atividades-list'),
    path('areas/', AreaList.as_view(), name='areas-list'),
    path('areas/<int:area_id>/', AreaDetalhes.as_view(), name='area-detalhes'),
    path('areas/<int:area_id>/subareas/', SubAreaArea.as_view(), name='area_sub_areas-detalhes'),

    path('subareas/', SubAreaList.as_view(), name='sub_area-list'),
    path('subareas/<int:sub_area_id>/', SubAreaDetalhes.as_view(), name='sub_area-detalhes')
]
