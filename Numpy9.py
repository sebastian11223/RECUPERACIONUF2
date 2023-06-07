import numpy as np
# EJERCICIO A)
def exercici1():
    # creamos array de hasta valor 49
    arry = np.arange(50)
    # construimos diagonal en nuevo array
    ndarray = np.diag(arry)
    # guardamos ndarray en archivo
    np.save('exercici1.npy', ndarray)
    return ndarray