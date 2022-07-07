from atividades.models import Plataforma


def listar_plataforma_area(usuario, area):
    return Plataforma.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)


def editar_plataforma(plataforma, plataforma_nova):
    plataforma.nome = plataforma_nova.nome
    plataforma.descricao = plataforma_nova.descricao
    plataforma.usuario = plataforma_nova.usuario
    for area in plataforma_nova.areas:
        plataforma.areas.add(area)
    plataforma.save(force_update=True)
    return plataforma
