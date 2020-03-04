import matplotlib.pyplot as plt
import LibreriaMatricesComplejas as l

def simulador(M,V,k):
    V_final = V[:]
    if k > 0:
        M_dinamica = potenciaMatriz(M,k)
        V_final = l.productoMatriz(M_dinamica,V)
    
    estado = []
    for i in range(len(V_final)):
        estado.append(V_final[i][0][0])
    index = list(range(len(estado)))
    plt.bar(index,estado)
    plt.show()

def ensamblar(M,N):
    return l.productoTensorial(M,N)
    

def potenciaMatriz(M,n):
    answer = M
    for i in range(n-1):
        answer = l.productoMatriz(answer,M)
    return answer

def main():
    
    M = [[(0,0),(0.2,0),(0.3,0),(0.5,0)],
         [(0.3,0),(0.2,0),(0.1,0),(0.4,0)],
         [(0.4,0),(0.3,0),(0.2,0),(00.1,0)],
         [(0.3,0),(0.3,0),(0.4,0),(0,0)]]

    N = [[(0,0),(1,0)],
         [(1,0),(0,0,)]]
    
    V = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]

    W = [[(0.5,0)],[(0.5,0)]]

    simulador(ensamblar(M,N),ensamblar(V,W),0)

main()
