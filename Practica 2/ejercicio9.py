un_string = input("Ingrese una palabra o frase: ")

es_heterograma = True

#Recorro el string en forma minuscula a traves de sus caracteres
#not letter.isspace() es para que no tenga en cuenta los espacios (los 
# cuales se pueden llegar a repetir)

for letter in un_string.lower():
    if (not letter.isspace())  and un_string.lower().count(letter) > 1:
        es_heterograma = False

if es_heterograma:
    print(f'{un_string} es heterograma')
else:
    print(f'{un_string} NO es heterograma')