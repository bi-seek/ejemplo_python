import csv

def obtener_10_mas_votados (csvreader):
    """Esta función retorna una lista con los 10 juegos más votados
    """
    lista = []
    next(csvreader)
    for linea in csvreader:
        lista.append(linea)
    lista.sort(key=lambda lista : lista[12],reverse=True)

    return lista[0:9]

def imagenes_10_mas_votados (csvreader):
    """Esta funcion solo imprime los datos de los 10
    juegos más votados
    """
    lista = obtener_10_mas_votados(csvreader)
    for elem in lista:
        print(elem[13])



archivo = open("bgg_db_1806.csv")
csvreader = csv.reader(archivo, delimiter=',')

imagenes_10_mas_votados(csvreader)

archivo.close()