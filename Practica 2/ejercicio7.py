
def transformar_en_numero (notas):
    """Esta funcion recibe una lista de digitos y
       los pasa a float uno por uno y los vuelve a
       almacenar en la misma lista
    """
    i = 0
    for una_nota in notas:
        notas[i] = float(una_nota)
        i = i + 1
    return None

def sumar_notas (evalu1,evalu2):
    notas = []
    for i in range(len(evalu1)):
        notas.append(evalu1[i] + evalu2[i])
    return notas

def obtener_promedio (notas_con_nombres):
    total = 0
    for notas in notas_con_nombres:
        total = total + notas[1]
    return total/(len(notas_con_nombres))

def calcular_alumnos_promedio (notas_con_nombres):
    """Esta funcion imprime aquellos alumnos con una nota
    menor al promedio :D
    """
    print('A continuacion se imprimiran aquellos alumnos cuya nota es menor al promedio')
    promedio = obtener_promedio(notas_con_nombres)
    print(f'El promedio es: {promedio}')
    for estudiante in notas_con_nombres:
        if (estudiante[1] < promedio):
            print(estudiante)
    return None

nombres = """'Agustin',
'Alan',
'Andrés',
'Ariadna',
'Bautista',
'CAROLINA',
'CESAR',
'David',
'Diego',
'Dolores',
'DYLAN',
'ELIANA',
'Emanuel',
'Fabián',
'Facundo',
'Facundo',
'FEDERICO',
'FEDERICO',
'GONZALO',
'Gregorio',
'Ignacio',
'Jonathan',
'Jonathan',
'Jorge',
'JOSE',
'JUAN',
'Juan',
'Juan',
'Julian',
'Julieta',
'LAUTARO',
'Leonel',
'LUIS',
'Luis',
'Marcos',
'María',
'MATEO',
'Matias',
'Nicolás',
'NICOLÁS',
'Noelia',
'Pablo'
'Priscila',
'TOMAS',
'Tomás',
'Ulises',
'Yanina'
"""
evalu1 = """
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""
evalu2 = """
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
 """

nombres = nombres.strip().split(',''\n')
evalu1 = evalu1.strip().split(',''\n')
evalu2 = evalu2.strip().split(',''\n')

transformar_en_numero(evalu1)
transformar_en_numero(evalu2)

#Crea una lista con los nombres y la suma de las dos evaluaciones
notas_con_nombres = list(zip(nombres,sumar_notas(evalu1,evalu2)))


print(notas_con_nombres)
calcular_alumnos_promedio(notas_con_nombres)