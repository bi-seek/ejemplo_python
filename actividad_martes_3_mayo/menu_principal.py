import PySimpleGUI as sg
from Android import menu_android
from Champions import menu_champions

def componentes():
    layout = [
        [sg.Text("¿Qué datos anailizamos?")],
        [sg.Button("Champions League Edición 2008/2009", size=(50,2), key='-champions-')],
        [sg.Button("Juegos de Android (Play Store)", size=(50,2), key='-android-')],
        [sg.Button("Salir", size=(50,2), key='-exit-')]
    ]

    ventana = sg.Window("Actividad 1 x Python Plus - TEORIA -", layout, no_titlebar=True)
    return ventana

def start():
    ventana = componentes()

    while True:
        events, values = ventana.read()

        if events == '-exit-':
            break

        elif events == '-champions-':
            ventana.hide()
            menu_champions.menu()
            ventana.un_hide()

        elif events == '-android-':
            ventana.hide()
            menu_android.menu()
            ventana.un_hide()

    ventana.close()