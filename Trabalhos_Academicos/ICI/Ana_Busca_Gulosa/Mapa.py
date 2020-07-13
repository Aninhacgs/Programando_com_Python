from Letras import Letras
from Adjacentes import Adjacentes

class Mapa:
    A = Letras('A',0)
    B = Letras('B',21)
    K = Letras('K',17)
    J = Letras('J',13)
    L = Letras('L',19)
    M = Letras('M',18)
    C = Letras('C',10)
    G = Letras('G',15)
    H = Letras('H',16)
    N = Letras('N',22)
    O = Letras('O',23)
    D = Letras('D',9)
    E = Letras('E',24)
    F = Letras('F',25)
    R = Letras('R',26)
    S = Letras('S',27)
    
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