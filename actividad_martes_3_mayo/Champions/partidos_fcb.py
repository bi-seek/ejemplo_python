import csv
import json

def generar_json():
    archivo = open("Champions/champions_league_08-09.csv", "r")
    datos = []
    for i in csv.DictReader(archivo):
        datos.append(dict(i))
    barc = list(filter(lambda x : 'FC Barcelona' in x['Team 1'] or 'FC Barcelona' in x['Team 2'], datos))
    print(barc)
    archivo.close()
    archivo_json = open("Champions/partidos_fc_barcelona.json", "w")
    json.dump(barc, archivo_json)
    archivo_json.close()

