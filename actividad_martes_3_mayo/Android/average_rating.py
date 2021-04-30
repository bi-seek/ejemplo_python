import csv
import json

def generar_json():
    archivo = open("Android/android-games.csv")
    datos = []
    for i in csv.DictReader(archivo):
        datos.append(dict(i))
    juegos = list(filter(lambda x : float(x['average rating']) >= 4.50, datos))
    archivo.close()
    print(juegos)
    archivo_json = open("Android/promedios_juegos.json", "w")
    json.dump(juegos, archivo_json)
    archivo_json.close()


