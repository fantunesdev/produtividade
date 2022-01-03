from django import template
import datetime

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='addclassplace')
def addclassplace(value, args):
    classe, placeholder = args.split(',')
    return value.as_widget(attrs={'class':classe, 'placeholder':placeholder})


@register.filter(name='em_horas')
def em_horas(tempo):
    """
    Converte um tempo em minutos, convertendo em dias, horas e minutos. Exemplo: 1521 = 1 dia, 01:22

    :param tempo: Tempo em minutos
    :return: Retorna dias horas e minutos no formato: %d dia, %hh%mm
    """
    hora = tempo // 60
    minuto = tempo % 60
    if(hora > 23):
        dia = hora // 24
        hora = hora % 24
        if(dia == 1):
            return "%d dia, %02d:%02d" % (dia, hora, minuto)
        else:
            return "%d dias, %02d:%02d" % (dia, hora, minuto)
    else:
        hora = tempo // 60
        return "%d:%02d" % (hora, minuto)


@register.filter
def get_item(dictionary, key):
    """
    Retorna um item de um dicionário passado no template com a seguinte sintaxe: {{ dicionario|get_item:chave }}, como
    por exemplo: {{ aluno|get_item:'nome' }}.

    :param dictionary: é o argumento que vem antes do |
    :param key: é o argumento que vem depois dos :
    :return: Retorna o ítem do dicionário segundo a chave passada
    """
    return dictionary.get(key)

@register.filter
def somar1(numero):
    return numero + 1

@register.filter
def subtrair1(numero):
    return numero - 1

@register.filter
def calcular_mes_anterior(mes_selecionado):
    mes_anterior = mes_selecionado - 1
    if mes_anterior == 0:
        mes_anterior = 12
    return mes_anterior

@register.filter
def calcular_mes_proximo(mes_selecionado):
    mes_proximo = mes_selecionado + 1
    if mes_proximo == 13:
        mes_proximo = 1
    return mes_proximo

@register.filter
def calcular_ano_mes_anterior(ano_mes_selecionado, mes_selecionado):
    ano = ano_mes_selecionado
    mes_anterior = mes_selecionado - 1
    if mes_anterior == 0:
        ano -= 1
    return ano

@register.filter
def calcular_ano_mes_proximo(ano_mes_selecionado, mes_selecionado):
    ano = ano_mes_selecionado
    mes_anterior = mes_selecionado + 1
    if mes_anterior == 13:
        ano += 1
    return ano

@register.filter
def calcular_semana_anterior(ano_semana_selecionada, semana_selecionada):
    semana_anterior = semana_selecionada - 1
    if semana_anterior == 0:
        ultimo_dia = datetime.datetime(ano_semana_selecionada, 12, 31)
        semana_anterior = ultimo_dia.isocalendar()[1]
    return semana_anterior

@register.filter
def calcular_semana_proxima(ano_semana_selecionada, semana_selecionada):
    semana_proxima = semana_selecionada + 1
    ultima_semana = datetime.datetime(ano_semana_selecionada, 12, 31).isocalendar()[1]
    if semana_proxima > ultima_semana:
        semana_proxima = 1
    return semana_proxima

@register.filter
def calcular_ano_semana_anterior(ano_semana_selecionada, semana_selecionada):
    ano = ano_semana_selecionada
    semana_anterior = semana_selecionada - 1
    if semana_anterior == 0:
        ano -= 1
    return ano

@register.filter
def calcular_ano_semana_proxima(ano_semana_selecionada, semana_selecionada):
    ano = ano_semana_selecionada
    semana_proxima = semana_selecionada + 1
    ultima_semana = datetime.datetime(ano_semana_selecionada, 12, 31).isocalendar()[1]
    if semana_proxima > ultima_semana:
        ano += 1
    return ano
