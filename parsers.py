

'''

Este módulo contiene todas las funciones auxiliares relacionadas con el parseo 
de tipos.

'''
from datetime import datetime


def parsea_holidays(holiday):
    '''
    Lee el valor de una cadena si contiene el literar 'Yes' retorna el booleano true , de lo contrario devuelve false

    '''
    if holiday == 'Yes':
        holiday = True
    else:
        holiday = False
    return holiday


def parsea_fecha(date):
    '''
    Recibe una cadena con una fecha en formato dia/mes/año y retorna 
    un objeto de tipo date con la fecha a la que se refiere la cadena de entrada.
    '''
    return datetime.strptime(date, '%Y-%m-%d').date()


def parsea_mes_numerico_str(num_mes):
    '''
    Recibe un str que representa el numero de mes del año y retorna un str con el nombre del mes.
    '''
    meses = {
        "1": 'Enero',
        "2": 'Febrero',
        "3": 'Marzo',
        "4": 'Abril',
        "5": 'Mayo',
        "6": 'Junio',
        "7": 'Julio',
        "8": 'Agosto',
        "9": 'Septiembre',
        "10": 'Octubre',
        "11": 'Noviembre',
        "12": 'Diciembre'
    }


    return meses[num_mes]
