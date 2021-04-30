import PySimpleGUI as sg
from Android import average_rating, juegos_5_estrellas, juegos_de_pago

def componentes():
    layout = [
        [sg.Button("Juegos con una puntuación media mayor o igual a 4.50", size=(50,2), key='-rating-')],
        [sg.Button("Juegos de pago", size=(50,2), key='-paid-')],
        [sg.Button("15 Juegos con más votaciones de 5 estrellas", size=(50,2), key='-stars-')]
    ]
    ventana = sg.Window("Juegos de Android (Play Store)", layout, no_titlebar=True)
    return ventana

def menu():
    ventana = componentes()

    while True:
        events, values = ventana.read()

        if events == '-rating-':
            ventana.hide()
            average_rating.generar_json()

        elif events == '-paid-':
            ventana.hide()
            juegos_de_pago.generar_json()

        elif events == '-stars-':
            ventana.hide()
            juegos_5_estrellas.generar_json()
        break
    ventana.close()
