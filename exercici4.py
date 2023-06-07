import numpy as np

def generar_array():
    # Crear una matriz de 4x3 con números aleatorios de 0 a 80
    matriz = np.random.randint(0, 81, size=(4, 3))
    return matriz

# Generar la matriz
matriz = generar_array()

# Mostrar la matriz por consola
print("Matriz:")
print(matriz)



#Modificar la matriz para obtener una nueva matriz de 3x4
nueva_matriz = np.transpose(matriz)
nueva_matriz = np.vstack((nueva_matriz[:-1], nueva_matriz[-1]))

# Mostrar la nueva matriz por consola
print("Nueva matriz con la fila cambiada:")
print(nueva_matriz)


#ultima parte
first_number = matriz[-1, -1]

#Modificar la matriz para obtener una nueva matriz con la última columna igual al primer numeroo
nueva_matriz = matriz.copy()
nueva_matriz[:, -1] = first_number

# Mostrar la nueva matriz por consola
print("Nueva matriz:")
print(nueva_matriz)