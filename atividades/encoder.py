import json


class Encoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('TempoArea__'): v for k, v in vars(o).items()}


def atividade_encoder(atividades):
    str_temp = '['
    for i in atividades:
        atividade_string = f'{{' \
                           f'"id": {i.id}, ' \
                           f'"data": "{i.data}", ' \
                           f'"area": {{' \
                           f'"id": {i.area.id},' \
                           f'"nome": "{i.area.nome}"' \
                           f'}}, ' \
                           f'"sub_area": {{' \
                           f'"id": {i.sub_area.id}, ' \
                           f'"nome": "{i.sub_area.nome}"' \
                           f'}}, ' \
                           f'"plataforma": "{i.plataforma}", ' \
                           f'"descricao": "{i.descricao}",' \
                           f'"tempo": {i.tempo}' \
                           f'}},'
        str_temp += atividade_string
    str_atividades = str_temp[:-1]
    str_atividades += ']'
    return str_atividades
