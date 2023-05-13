from matplotlib import pyplot as plt
from parsers import * 

'''
En este módulo se incluyen las funciones relacionadas con el dibujo de gráficas
'''


def grafica_barras_usuarios_meses(resgistro , año):
    '''
    Función que recibe una lista de tupla de tipo BikeStats y un año , genera una gráfica de barras . Las etiquetas del eje x esta dada por la lista meses , en el eje y se contruyen las barras
    con la lista usuarios (sumatorio de usuarios de cada  mes del año que recibe).

    -Parámetros: 
        0.registros : es de tipo lista , contiene tuplas de tipo BikeStats.
    
    -Valor que devuelve:
        Una gráfiica de barras.

    '''
    titulo = f"Tendencia del numero de usuarios por meses en el año {año}"
    meses = list()
    usuarios = list()
    dic_aux = {}
    for r in resgistro:
        if año == r.date.year :
            mes = parsea_mes_numerico_str(str(r.date.month))
            if mes not in dic_aux:
                
                dic_aux[mes] = r.users
            else :
                dic_aux[mes] += r.users
        
    for c,v in dic_aux.items():
        meses.append(c)
        usuarios.append(v)
    
    if len(meses)<1 :
        return (f"No hay registros para {año}")

    plt.title(titulo)
    plt.bar(meses, usuarios)
    plt.show()
    return (dic_aux)