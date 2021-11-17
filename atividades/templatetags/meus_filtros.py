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
