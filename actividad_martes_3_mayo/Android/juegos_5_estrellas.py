import csv
import json

def generar_json():
    archivo = open("Android/android-games.csv")
    datos = []
    for i in csv.DictReader(archivo):
        datos.append(dict(i))
    juegos_max = sorted(datos, key=lambda x : x['5 star ratings'], reverse=True)
    juegos = juegos_max[0:15]
    archivo.close()
    print(juegos)
    archivo_json = open("Android/juegos_5_estrellas.json", "w")
    json.dump(juegos, archivo_json)
    archivo_json.close()