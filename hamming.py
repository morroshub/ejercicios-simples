# Definir dos palabras :
palabra1 = "músicabuela"
palabra2 = "públicocasa"

# Asegurarse de que las palabras tengan la misma longitud (11 caracteres)
if len(palabra1) != len(palabra2):
    print("ERROR! Las palabras deben tener la misma longitud para calcular la distancia de Hamming.")
else:
    # Inicializar la variable para contar las diferencias
    distancia = 0

    # Iterar a través de los caracteres de las dos palabras y contar las diferencias
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1

    # Imprimir la distancia de Hamming
    print(f"La distancia de Hamming entre '{palabra1}' y '{palabra2}' es {distancia}.")
