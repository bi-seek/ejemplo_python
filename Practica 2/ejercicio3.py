import string

unTexto = """Cactus suaviza mis yemas con su piel 
Tiene cien años, solo florece una vez 

En tu nombre, en tu nombre 

Y tiene un veneno, mas amargo que la hiel 
Con solo invocarte, voy a convertirme en miel 

En tu nombre, en tu nombre 

Cuando te busco 
no hay sitio en donde no estes 

Y los médanos, serán témpanos 
en el vértigo, de la eternidad 
Y los pájaros, serán árboles 
En lo idéntico, de la soledad 

En tu nombre, en tu nombre 

Y cuando te busco 
no hay sitio en donde no estes 

Y los médanos, serán témpanos 
en el vértigo, de la eternidad 
Y los pájaros, serán árboles 
En lo idéntico, de la soledad 

En tu nombre, en tu nombre 
"""

lista = unTexto.split(" ")

laLetra = input('Ingrese una letra: ')

if laLetra in string.ascii_letters:
    print('Nice')
    for word in lista:
        if laLetra == word[0]:
            print(word)
else:
    print('ERROR')