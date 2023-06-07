import numpy as np
import Numpy9
import exercici2
import exercici3
import exercici4
from exercici2 import ex2part1
from exercici2 import ex2part2
from exercici2 import ex2part3
from exercici3 import exercici3array, exercici3arraymin, exercici3arraymax
from ejercicio4 import generar_array


# Exercici 1
print("Exercici 1")
# ejercicio 1 - mostramos la matriz
print('impresion la array: ', Numpy9.exercici1())
# ejercicio 2 - dimensión de matriz
print('Dimension de la matriz: ', Numpy9.exercici1().ndim)
# ejercicio 3 - tamaño de la matriz
print('Tamaño de la matriz: ', Numpy9.exercici1().shape)
# ejercicio 4 - numero total de elementos
print('Num total de elementos: ', Numpy9.exercici1().size)
# ejercicio 5 - tipos de elementos internos
print('Tipos de elementos internos: ', Numpy9.exercici1().dtype)


#exercici2
# Llamar a la función ex2part1() y mostrar el resultado
result1 = ex2part1()
print("Resultado de ex2part1():")
print(result1)
print("Num total de elementos:", result1.size)
print("Dimension de la matriz:", result1.ndim)
print("Tipo de elementos internos:", result1.dtype)
print("Tamaño de la matriz:", result1.shape)

# Llamar a la función ex2part2() y mostrar el resultado
result2 = ex2part2()
print("Resultado de ex2part2():")
print(result2)
print("Num total de elementos:", result2.size)
print("Dimension de la matriz:", result2.ndim)
print("Tipo de elementos internos:", result2.dtype)
print("Tamaño de la matriz:", result2.shape)

# Llamar a la función ex2part3() y mostrar el resultado
result3 = ex2part3()
print("Resultado de ex2part3():")
print(result3)
print("Num total de elementos:", result3.size)
print("Dimension de la matriz:", result3.ndim)
print("Tipo de elementos internos:", result3.dtype)
print("Tamany del array:", result3.shape)

#exercici3
# Obtener la matriz indicada por el usuario
matriz = exercici3array()

# Obtener el valor máximo y mínimo de la matriz
maximo = exercici3arraymax(matriz)
minimo = exercici3arraymin(matriz)

# Mostrar la matriz, valor máximo y valor mínimo
print("Matriz indicada por el usuario:")
print(matriz)
print("Valor maximo:", maximo)
print("Valor mín:", minimo)


#parte 4

# Generar la matriz
matriz = generar_array()

# Mostrar la matriz por consola con un mensaje
print("Matriz generada:")
print(matriz)

# Modificar la matriz para obtener una nueva matriz de 3x4
nueva_matriz = np.transpose(matriz)
nueva_matriz = np.vstack((nueva_matriz[:-1], nueva_matriz[-1]))

# Mostrar la nueva matriz por consola con un mensaje
print("Nueva matriz con la fila cambiada:")
print(nueva_matriz)

# Obtener el primer número de la última columna
first_number = matriz[-1, -1]

# Modificar la matriz para obtener una nueva matriz con la última columna igual al primer número
nueva_matriz = matriz.copy()
nueva_matriz[:, -1] = first_number

# Mostrar la nueva matriz por consola con un mensaje
print("Nueva matriz con la última columna igual al primer número:")
print(nueva_matriz)
