''''
En el siguiente ejercicio, es necesario realizar un conteo de los siguientes caracteres para los siguientes textos:

'e', 'c' , 'p'

'Cleopatra echada, al César puedo traicionar
Por un minuto de tu atención, ingenua esfinge
Tu perfumada suavidad, me hace vivir extrañándote'

'''

texto = "Cleopatra echada, al César puedo traicionar Por un minuto de tu atención, ingenua esfinge Tu perfumada suavidad, me hace vivir extrañándote"


'Enfoque usando un diccionario y un bucle for'

# Se crea un diccionario para contar ocurrencias
conteo_caracteres = {'c': 0, 'p': 0, 'e': 0}

# Convertir el texto a minúsculas para que coincida con mayúsculas y minúsculas
texto = texto.lower()

# Iterar sobre el texto y contar las ocurrencias
for caracter in texto:
    if caracter in conteo_caracteres:
        conteo_caracteres[caracter] += 1

# Imprimir el resultado
print(conteo_caracteres)

'Enfoque usando count()'

# Contar las ocurrencias de 'c', 'p' y 'e' usando el método count()
conteo_c = texto.count('c')
conteo_p = texto.count('p')
conteo_e = texto.count('e')

# Crear una lista con los conteos
lista_conteo = [conteo_c, conteo_p, conteo_e]

# Imprimir el resultado
print(lista_conteo)



'Dado el texto anterior, realizar un conteo de palabras.'

# Convertir el texto a minúsculas para que coincida con mayúsculas y minúsculas
texto = texto.lower()

# Palabras que deseas contar
palabras_a_contar = ['cleopatra', 'césar', 'traicionar', 'minuto', 'atención', 'esfinge', 'suavidad', 'vivir']

# Inicializar un diccionario para contar las ocurrencias de palabras
conteo_palabras = {palabra: 0 for palabra in palabras_a_contar}

# Dividir el texto en palabras
palabras_en_texto = texto.split()

# Contar las ocurrencias de palabras
for palabra in palabras_en_texto:
    palabra = palabra.strip('.,')  # Eliminar signos de puntuación alrededor de las palabras
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1

# Crear una lista con los conteos
lista_conteo = [conteo_palabras[palabra] for palabra in palabras_a_contar]

# Imprimir el resultado
print(lista_conteo)