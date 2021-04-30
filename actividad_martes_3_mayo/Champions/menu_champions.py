import PySimpleGUI as sg
from Champions import semifinales, partidos_fcb, partidos_rmc

def componentes():
    layout = [
        [sg.Button('Semifinales', size=(50,2), key='-sf-')],
        [sg.Button('Partidos ganados por FC Barcelona', size=(50,2), key='-fcb-')],
        [sg.Button('Partidos ganamos por Real Madrid', size=(50,2), key='-rmc-')],
    ]
    ventana = sg.Window("Champions League 2008/2009", layout, no_titlebar=True)

    return ventana

def menu():
    ventana = componentes()

    while True:
        events, values = ventana.read()

        if events == '-sf-':
            ventana.hide()
            semifinales.generar_json()

        elif events == '-fcb-':
            ventana.hide()
            partidos_fcb.generar_json()

        elif events == '-rmc-':
            ventana.hide()
            partidos_rmc.generar_json()

        break
    ventana.close()