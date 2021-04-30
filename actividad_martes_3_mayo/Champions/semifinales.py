import csv
import json

def generar_json():
    archivo = open("Champions/champions_league_08-09.csv")
    datos = []
    for i in csv.DictReader(archivo):
        datos.append(dict(i))
    semis = list(filter(lambda x : 'Semifinals' in x['Round'], datos))
    print(semis)
    archivo.close()
    archivo_json = open("Champions/semifinales.json", "w")
    json.dump(semis, archivo_json)
    archivo_json.close()