def actualizar_linea (linea, j, nuevo_valor):
    #aux es un string con la info actualizada
    aux = ''

    for i in range(len(linea)):
        #j es la posicion donde debo insertar el nuevo valor        
        if i == j:
            aux = aux + nuevo_valor
        else:
            aux = aux + linea[i]
    
    return aux

def incrementar (area, i, j):

    #incremento la casilla
    aux = str ( int(area[i][j]) + 1 )

    #actualizo la linea en el area
    area[i] = actualizar_linea (area[i], j, aux)

    return None

def verificar_linea (area, i, j):

    #Si hay espacio a la izq y el elemento de esa pos no es una mina
    if ((j - 1 >= 0) and (area[i][j - 1] != "*")):
        incrementar(area, i, j - 1)
    
    #Si hay espacio a la der y el elemento de esa pos no es una mina
    if ((j + 1 < len(area[i])) and (area[i][j + 1] != "*")):
        incrementar(area, i, j + 1)
    
    #Si el elemento actual no es una mina
    if (area[i][j] != "*"):  
        incrementar(area, i, j)

    return None


def verificar_alrededor (area, i, j):

    #Si hay elementos arriba
    if (i - 1 >= 0):
        verificar_linea(area, i - 1, j)
        #verifico los elementos de la linea de arriba
    
    #Si hay elementos abajo
    if (i + 1 < len(area)):
        verificar_linea(area, i + 1, j)
        #verifico los elementos de la linea de abajo
    
    verificar_linea(area, i, j)
    #verifico los elementos de la linea actual
    
    return None


def buscar_minas (area):

    for i in range(len(area)):

        for j in range(len(area[i])):

            if area[i][j] == "*":
                verificar_alrededor(area, i, j)


def imprimir_area (area):
    for elem in area:
        print(elem)
    
    return None

def modificar_area (area):
    
    aux = []
    #Recorro por string
    for elem in area:
        linea = ''
        #recorro cada caracter del string
        for i in elem:
            if (i == "-"):
                linea +=  "0"
            else:
                linea +=  "*"
        aux.append(linea)
    
    
    return aux
      

area = [
'-*-*-',
'--*--',
'----*',
'*----',
]

#Antes
imprimir_area(area)
area = modificar_area(area)

imprimir_area(area)

buscar_minas(area)

#Despues
imprimir_area(area)