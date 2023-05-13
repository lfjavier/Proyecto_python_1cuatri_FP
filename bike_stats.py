'''
Bikes Stats
@author: Javier Luis Fernandez
'''


from collections import defaultdict, namedtuple
import csv
from matplotlib import pyplot as plt
from parsers import *

BikeStats = namedtuple(
    'BikeStats', 'date,weekday,weathersit,holiday,temp,hum,windspeed,users')

##########################################################################################################


def lee_datos_bikestats(ruta_archivo):
    '''
    Lee un fichero de datos csv con informacion sobre el recuento diario y por hora de bicicletas de alquiler 
    entre los años 2011 y 2012 en el sistema de bicicletas compartidas de Capital
    con la información meteorológica y estacional correspondiente.

    -Patámetros : 
        0. ruta_archivo : es de tipo str , contiene le ruta del archivo CSV.

    -Valor que devuelve:
        Esta función devuelve una lista de tuplas de tipo BikeStats , con la información que contiene el fichero.
    '''

    res = list()
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # me salto la cabecera del archivo csv
        for date, weekday, weathersit, holiday, temp, hum, windspeed, users, in lector:
            # conversion de los tipos
            date = parsea_fecha(date)
            temp = float(temp)
            hum = float(hum)
            windspeed = float(windspeed)
            users = int(users)
            holiday = parsea_holidays(holiday)

            res.append(BikeStats(date, weekday, weathersit,
                       holiday, temp, hum, windspeed, users))
    return res
##################################################################################################################

    # 2 ENTREGA

##################################################################################################################


def filtra_dias_holidays_mes(datos, año_i, mes_i):
    '''
    Recibe una lista de tuplas de tipo BikeStats , y filtra los dias que son holidays(es decir dias de fiestas) en uno o varios meses.

    -Parámetros : 
        0. datos : es de tipo lista , contiene tuplas de tipo BikeStats
        1. año_i : es de tipo str , contiene el año donde se filtrará por holidays
        2. mes_i : es de tipo str , contiene el mes  donde se filtrará por holidays

    -Valor que devuelve:
        Devuelve una lista de tuplas de tipo BikeStats , con los registros de dias que son holidays durante el mes del año introducido

    '''
    res = list()
    for dato in datos:
        mes = str(dato.date.month)
        año = str(dato.date.year)
        nombre_mes = parsea_mes_numerico_str(mes)

        if nombre_mes.lower() == mes_i.lower() and año == año_i and dato.holiday == True:
            res.append(dato)
    return res
#######################################################################################################################################################################


def media_usuarios_por_dia(registros, dia):
    '''
     Recibe una lista de tuplas de tipo BikeStats y un día de la semana , y calcula la media de usuarios de ese día , es decir ,por ejemplo la media de usuarios un lunes.

    -Parámetros :
        0. registros : es de tipo lista , contiene tuplas de tipo BikeStats.
        1. dia : es de tipo str , contiene el día por el cual se filtrará para hacer la media.

    -Valor que devuelve: 
        Devuelve un valor float la media de usuarios del día seleccionado.
    '''
    cont = 0
    suma_usuarios = 0

    for r in registros:
        if r.weekday.lower() == dia.lower():
            cont += 1
            suma_usuarios += r.users
    return (suma_usuarios / cont)

#######################################################################################################################################################################


def max_min_usuarios_tipodia(registros, tipodia):
    '''
    Función que recibe una lista de tuplas de tipo BikeStats y un str con el tipo de dia y devuelve el registro con mayor número de usuarios y el registro con menor número de usuarios de entre todos los registros que tienen ese tipo de dia .
    -Parámetros : 
        0. registros : es de tipo lista , contiene tuplas de tipo BikeStats.
        1. tipodia : es de tipo str , contiene el tipo de dia e cuanto a meteorología por el cual se filtra los registros.


    -Valor que devuelve: 
        Devuelve dos tuplas las cuales tienen el mismo tipo de día que le llega a la función y una con el  mayor número de usuarios otra con el menor .
    '''
    res = list()

    for r in registros:
        if r.weathersit == tipodia:
            res.append(r)
    return (max(res, key=lambda e: e[7])), (min(res, key=lambda e: e[7]))

#######################################################################################################################################################################


def usuarios_temperatura(registros, temp, n):
    '''
    Función que recibe una lista de tuplas  de tipo BikeStats y una temperatura y devuelve una lista de tuplas con los n  registros con la temperaturas mas cercanas tanto mayores como menores.

    -Parámetros:
        0. registros : es de tipo lista , contiene tuplas de tipo BikeStats.
        1. temp : es de tipo float , contiene la temperatura normalizada en celsius.
        2. n : es de tipo int , contiene el numero de tuplas  que contendrá la lista.

    -Valor que devuelve:
        Devuelve una lista de n tuplas de tipo BikeStats
    '''

    # abs es para restar en valor absoluto
    '''
    lista_ordenada = sorted(abs(c.temp - float(temp)) for c in registros)

    res = list()

    for r in registros:
        resta = abs(r.temp - float(temp))
        if resta in lista_ordenada[0:n]:
            res.append(r)
        if len(res) == n:
            return res
    '''
    lista_ordenada = sorted(abs(c.temp - float(temp) , ) for c in registros)
    return (lista_ordenada[0:n])
    

#######################################################################################################################################################################


def agrupa_por_dia_semana(registros):
    '''
    Función que recibe una lista de tuplas  de tipo BikeStats , y devuelve un diccionario donde se agrupa por día de la semana , la clave sería el día de la semana y valor una lista de tuplas con los registros pertenecientes al día de su clave.

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Diccionario donde las claves son str , los valores lista de tuplas tipo BikeStats.

    '''

    res = {}

    for r in registros:
        if r.weekday not in res:
            res[r.weekday] = [r]
        else:
            res[r.weekday].append(r)

    return res


#######################################################################################################################################################################

    # 3º ENTREGA

#######################################################################################################################################################################


def total_usuarios_por_año(registros):
    '''
    Función que recibe una lista de tuplas de tipo BikeStats , y devuelve un diccionario donde se agrupa por año y cuenta el total de usuarioas
    en ese año . 

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Devuelve un diccionario donde las claves son int , y los valores de tipo int. 
    '''

    res = {}
    for r in registros:
        
        if r.date.year not in res:
            res[r.date.year] = r.users
        else:
            res[r.date.year] += r.users

    return res

################################################################################################################################################################


def tendencia_meteorologica(registros):
    '''
    Función que recibe una lista de tuplas  de tipo BikeStats y devuelve el tipo de dia meteorológico que mas se repite 
    en los registros que tenemos.

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Una lista  de la forma (str,int) .
    '''

    res = {}
    for r in registros:
        if r.weathersit not in res:
            res[r.weathersit] = 1
        else:
            res[r.weathersit] += 1
    maximo = max(res.items(), key=lambda e: e[1])
    return maximo

################################################################################################################################################################


def maximo_usuarios_por_año_mes(registros):
    '''
    Función que recibe una lista de tuplas de tipo BikeStats y devuelve un diccionario donde se agrupa por año y mes y muestra 
    el numero maximo de usuarios que hubo en un dia de ese mes .

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Diccionario donde las claves son tuplas (int , str) , los valores tipo int.
    '''
    aux = {}

    for r in registros:

        mes = parsea_mes_numerico_str(str(r.date.month))
        año = r.date.year

        if (año, mes) not in aux:
            aux[(año, mes)] = [r]
        else:
            aux[(año, mes)].append(r)

    res = {}
    for c, v in aux.items():
        res[c] = max(v, key=lambda e: e[7])[7]

    return res

################################################################################################################################################################


def n_weathersit_min_temperatura(registros, n):
    '''
    Función que recibe una lista de tupla de tipo BikeStats y devuelve un diccionario donde se agrupa por tipo meteorológico de día y se devuelven los n días de
    ese tipo con menor temperatura .

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Diccionario donde las claves son str , los valores listas de tuplas  (datetime.date , float).

    '''

    aux = {} #declaro diccionario vacío
    for r in registros: #recorro la lista de tuplas que recibe la funcion
        if r.weathersit not in aux: 
        # si r.weathersit no esta en el diccionario aux lo asigno como clave y valor vacio
            aux[r.weathersit] = []
        else:
            #si la clave ya existe en el diccionario le asigno el valor de esa clave : la fecha (r.date) y la temperatura (r.temp)
            aux[r.weathersit].append((r.date, r.temp)) 

    res = {} #declaro un diccionario vacío
    for c, v in aux.items(): #recorro el diccionario aux 
        if n < 1:
            res[c] = sorted(v, key=lambda e: e[1])[:2] #si n es menor que 1 es decir 0 o negativo  asigno a la clave el valor de las dos dias menores temperaturas
        else:                                          # esto lo hago ordenando de menor a mayor la lista contenida en el valor de la clave y cogiendo los 2 primeros de la lista 
            res[c] = sorted(v, key=lambda e: e[1])[:n] # aqui hago lo mismo pero cuando n si es valido para mi es decir mayor de 0
    return res #retorno el diccionario res

  ################################################################################################################################################################

