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
