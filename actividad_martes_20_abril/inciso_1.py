import csv

def listar_juegos_de_cartas (csvreader):
    """
    Esta función recibe el archivo csv separado por ','
    y lista en pantalla aquellos juegos que se juegen con
    menos de 3 personas y que sean juegos de cartas
    """
    next(csvreader)
    for linea in csvreader:
        if int(linea[5]) < 3 and "Card Game" in linea[17]:
            print(f"{linea[3]} es un juego de cartas que se juega con menos de 3 jugadores")

archivo = open("bgg_db_1806.csv")
csvreader = csv.reader(archivo, delimiter=',')

listar_juegos_de_cartas(csvreader)

archivo.close()