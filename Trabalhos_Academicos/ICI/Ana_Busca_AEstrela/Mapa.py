from Letras import Letras
from Adjacentes import Adjacentes

class Mapa:
    A = Letras('A',0,0)
    B = Letras('B',21,11)
    K = Letras('K',17,27)
    J = Letras('J',13,33)
    L = Letras('L',19,29)
    M = Letras('M',18,28)
    C = Letras('C',10,20)
    G = Letras('G',15,10)
    H = Letras('H',16,26)
    N = Letras('N',22,32)
    O = Letras('O',23,13)
    D = Letras('D',9,39)
    E = Letras('E',24,14)
    F = Letras('F',25,35)
    R = Letras('R',26,36)
    S = Letras('S',27,37)
    
    '''Nós Adjacentes do nó raiz A'''
    A.AddLetrasAdjacentes(Adjacentes(B))
    A.AddLetrasAdjacentes(Adjacentes(C))
    A.AddLetrasAdjacentes(Adjacentes(D))
    
    '''Nós Adjacentes do nó B'''
    B.AddLetrasAdjacentes(Adjacentes(K))
    B.AddLetrasAdjacentes(Adjacentes(J))
    
    '''Nós Adjacentes do nó C'''
    C.AddLetrasAdjacentes(Adjacentes(G))
    C.AddLetrasAdjacentes(Adjacentes(H))
    
    '''Nós Adjacentes do nó D'''
    D.AddLetrasAdjacentes(Adjacentes(E))
    D.AddLetrasAdjacentes(Adjacentes(F))
    
    
    '''Nós Adjacentes do nó J'''
    J.AddLetrasAdjacentes(Adjacentes(L))
    J.AddLetrasAdjacentes(Adjacentes(M))
    
    '''Nós Adjacentes do nó G'''
    G.AddLetrasAdjacentes(Adjacentes(N))
    G.AddLetrasAdjacentes(Adjacentes(O))
    
    
    '''Nós Adjacentes do nó F'''
    F.AddLetrasAdjacentes(Adjacentes(R))
    F.AddLetrasAdjacentes(Adjacentes(S))