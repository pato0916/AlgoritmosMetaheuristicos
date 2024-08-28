import sys
import numpy as np

if len(sys.argv) == 7:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    ite = int(sys.argv[4])
    pc = float(sys.argv[5]) / 100
    pm = float(sys.argv[6]) / 100
    print(semilla, n, p, ite, pc, pm)
else:
    print("Error en la entrada de los parámetros")
    print("Los parámetros a ingresar son: semilla tamañoTablero TamañoPoblacion NroIteraciones ProbCruza ProbMutacion")
    sys.exit(0)

np.random.seed(semilla)


poblacion = np.zeros((p,n), int)
for i in range(p):
    fila = np.arange(n)  # Crea un arreglo de 0 a n-1
    np.random.shuffle(fila)  
    poblacion[i] = fila  # Asigna la fila barajada a la matriz
print(poblacion)
        
