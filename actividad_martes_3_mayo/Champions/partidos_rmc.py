import csv
import json

def generar_json():
    archivo = open("Champions/champions_league_08-09.csv")
    datos = []
    for i in csv.DictReader(archivo):
        datos.append(dict(i))
    madrid = list(filter(lambda x : 'Real Madrid CF' in x['Team 1'] or 'Real Madrid CF' in x['Team 2'], datos))
    print(madrid)
    archivo.close()
    archivo_json = open("Champions/partidos_real_madrid.json", "w")
    json.dump(madrid, archivo_json)
    archivo_json.close()

