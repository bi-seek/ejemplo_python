unaFrase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple"""

print(unaFrase)
lista = []

#Separo las palabras para cuando recorra el string
#tome las palabras, no las letras de cada palabra
unaFrase = unaFrase.split(' ')

for word in unaFrase:
    print(word)
    if word.islower() and unaFrase.count(word) == 1:
        lista.append(word)

print(lista)