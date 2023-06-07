import numpy as np

def exercici3array():
    # Pedir al usuario el valor de x e y como enteros
    x = int(input("Enter variable x: "))
    y = int(input("Enter variable y: "))

    # Crear una matriz con valores aleatorios entre 0 y 100
    arr = np.random.randint(0, 101, size=(x, y))

    # Imprimir la matriz resultante
    print(arr)

    # Redimensionar la matriz a una nueva forma (4 filas, 3 columnas)
    newarr = arr.reshape(4, 3)

    # Imprimir la nueva matriz redimensionada
    print(newarr)

    return newarr

def exercici3arraymin(arr):
    # Valor mínimo de la matriz
    min_value = np.min(arr)
    return min_value

def exercici3arraymax(arr):
    # Valor máximo de la matriz
    max_value = np.max(arr)
    return max_value

matriz = exercici3array()

# Obtener el valor máximo y mínimo de la matriz
maximo = exercici3arraymax(matriz)
minimo = exercici3arraymin(matriz)

# Mostrar los valores máximo y mínimo
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
