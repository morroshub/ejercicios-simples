''''
Dadas las siguientes palabras, invertir las cadenas de cualquier forma.

'reconocer'
'anilina'
'radar'

tambien esta oracion :
'Ana, la niña del vestido seda, reconoce a su mamá'.

'''

palabra = "reconocer"
palabra_al_reves = ""
for letra in palabra:
    palabra_al_reves = letra + palabra_al_reves
print(palabra_al_reves)

'En este enfoque, utilizamos un bucle for para recorrer cada letra de la palabra original en orden inverso y construimos la palabra invertida letra por letra.'

palabra = "anilina"
lista_de_letras = list(palabra)
lista_de_letras.reverse()
palabra_al_reves = ''.join(lista_de_letras)
print(palabra_al_reves)

' Aquí, convertimos la palabra en una lista de letras, invertimos la lista con el método reverse y luego convertimos la lista invertida en una cadena nuevamente. Este método funciona para cualquier palabra.'



def invertir_palabra(palabra):
    return palabra[::-1]

palabra = "radar"
palabra_al_reves = invertir_palabra(palabra)
print(palabra_al_reves)

'En este enfoque, definimos una función llamada invertir_palabra que toma una palabra como entrada y la invierte utilizando la técnica de "slicing" con [::-1]. Luego, llamamos a esta función para invertir la palabra original. Esta es una forma eficiente y general de invertir palabras.'