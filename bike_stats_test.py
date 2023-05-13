'''
Created on 11 oct. 2021
@author: Javier Luis Fernandez
'''


from bike_stats import *
from graficas import *

###########################################################################################################


def test_lee_datos_bikestats(datos):
    """
   Muestra el número de elementos de datos, los 3 primeros registros y los 3 últimos registros.

   @param datos: lista de tuplas con información de las estadísticas del aquiler de bicicletas.
   @type datos: list(BikeStats)
   """

    print("\n########################### Test de lee_datos_bikestats ############################################################################################### \n")
    print("Registros obtenidos :")
    print(len(datos))

    print("\nMuestro los 3 primeros")
    print(datos[:3])

    print("\nMuestro los 3 ultimos")
    print(datos[-3:])
    print(f"\n###################################################################################################################################################### \n")

###########################################################################################################


def test_filtra_dias_holidays_mes(datos):
    print(f"\n########################### TEST FUNCION FILTRA_DIAS_HOLIDAYS_MES #################################################################################### \n")
    año_i ="2011"
    mes_i = "noviembre"
    print(filtra_dias_holidays_mes(datos, año_i, mes_i))
    print(f"\n###################################################################################################################################################### \n")

###########################################################################################################

def test_media_usuarios_por_dia(datos):
    
    dia_i = "monday"
    print(f"\n########################### TEST FUNCION media_usuarios_por_dia ###################################################################################### \n")
    print(f"\nLa media de usuarios del dia {dia_i} es : {media_usuarios_por_dia(datos, dia_i)}")
    print(f"\n###################################################################################################################################################### \n")

###########################################################################################################

def test_max_min_usuarios_tipodia (datos):
    tipodia = "Cloudy"
    print(f"\n########################### TEST FUNCION max_min_usuarios_tipodia #################################################################################### \n")
    print(f"{max_min_usuarios_tipodia(datos, tipodia)}")
    print(f"\n###################################################################################################################################################### \n")

############################################################################################################
def test_usuarios_temperatura(datos):
    temp = 0.541
    print(f"\n########################### TEST FUNCION usuarios_temperatura ######################################################################################## \n")
    print(f"\n{usuarios_temperatura(datos , temp , n=4)}")
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_agrupa_por_dia_semana (datos):
    print(f"\n########################### TEST FUNCION agrupa_por_dia_semana  ##################################################################################### \n")
    result = agrupa_por_dia_semana(datos)
    for c,v in result.items():
        print(f"Los 3 primeros registros del {c}: \n{v[:3]}\n") #para que se visualice cada pareja clave-valor una debajo de otra. Solo muestro los 3 primeros
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_total_usuarios_por_año(datos):
    print(f"\n########################### TEST FUNCION total_usuarios_por_año ###################################################################################### \n")
    result = total_usuarios_por_año(datos)
    print(f"El registro de usuarios por año es {result}")
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_tendencia_meteorologica(datos):
    print(f"\n########################### TEST FUNCION tendencia_meteorologica #################### \n")
    result = tendencia_meteorologica(datos)
    print(f"{result[0]} es el tipo de día que mas se ha repetido con un total de {result[1]} días.")
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_maximo_usuarios_por_año_mes(datos):
    print(f"\n########################### TEST FUNCION maximo_usuarios_por_año_mes ################################################################################# \n")
    result = maximo_usuarios_por_año_mes(datos)
    for c,v in result.items() :
        print(f"{c} maximo de usuarios registrados en un día {v}")   
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_n_weathersit_min_temperatura(datos):
    n=2
    print(f"\n########################### TEST FUNCION n_weathersit_min_temperatura ############################################################################### \n")
    result = n_weathersit_min_temperatura(datos , n)
    for c,v in result.items() :
        print(f"Para: {c} \nLos {len(v)} dias con menos temperaturas son {v}\n")
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################
def test_grafica_barras_usuarios_meses(datos):
    print(f"\n########################### TEST FUNCION total_usuarios_por_año ##################################################################################### \n")
    result = grafica_barras_usuarios_meses(datos , año = 2011)
    print(f" {result}")
    print(f"\n###################################################################################################################################################### \n")
############################################################################################################




ruta_archivo = r'data\bike_sharing_stats_1.csv'
datos = lee_datos_bikestats(ruta_archivo)
#test_lee_datos_bikestats(datos)
#test_filtra_dias_holidays_mes(datos)
#test_media_usuarios_por_dia(datos)
#test_max_min_usuarios_tipodia (datos)
test_usuarios_temperatura(datos)
#test_agrupa_por_dia_semana (datos)
#test_total_usuarios_por_año(datos)
#test_tendencia_meteorologica(datos)
#test_maximo_usuarios_por_año_mes(datos)
#test_n_weathersit_min_temperatura(datos)
#test_grafica_barras_usuarios_meses(datos)

