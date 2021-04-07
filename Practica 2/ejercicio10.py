valor_1 = "AEIOULNRSTaeioulnrst"
valor_2 = "DGdg"
valor_3 = "BCMPbcmp"
valor_4 = "FHVWYfhvwy"
valor_5 = "Kk"
valor_8 = "JXjx"
valor_10 = "QZqz"

palabra = input("Ingrese una palabra")
dicci = {palabra : 0}

for letter in palabra:
    if letter in valor_1:
        dicci[palabra] = dicci[palabra] + 1
    elif letter in valor_2:
        dicci[palabra] = dicci[palabra] + 2
    elif letter in valor_3:
        dicci[palabra] = dicci[palabra] + 3
    elif letter in valor_4:
        dicci[palabra] = dicci[palabra] + 4
    elif letter in valor_5:
        dicci[palabra] = dicci[palabra] + 5
    elif letter in valor_8:
        dicci[palabra] = dicci[palabra] + 8
    elif letter in valor_10:
        dicci[palabra] = dicci[palabra] + 10

print(f'La cantida de puntos es: {dicci[palabra]}')
