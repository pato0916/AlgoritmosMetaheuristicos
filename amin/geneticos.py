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

for i in range(p):
     print(i+1,": ", np.random.randint(1,p)) 
     print(i+1,": ", np.random.rand())
           
poblacion = np.zeros((p,n), int)

print(poblacion)
        
