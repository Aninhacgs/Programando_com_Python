from Letras import Letras
from Adjacentes import adjacentes

class Mapa:
    A = Letras("A")
    B = Letras("B")
    C = Letras("C")
    D = Letras("D")
    E = Letras("E")
    F = Letras("F")
    G = Letras("G")
    H = Letras("H")
    I = Letras("I")
    J = Letras("J")
    L = Letras("L")
    M = Letras("M")
    N = Letras("N")
    O = Letras("O")
    P = Letras("P")
    Q = Letras("Q")
    S = Letras("S")
    R = Letras("R")
    
    '''Estados ligados ao estado A'''
    A.addCidadesAdjacentes(adjacentes(B))
    A.addCidadesAdjacentes(adjacentes(E))

    '''Estados ligados ao estado B'''
    B.addCidadesAdjacentes(adjacentes(C))
    B.addCidadesAdjacentes(adjacentes(F))

    '''Estados ligados ao estado F'''
    F.addCidadesAdjacentes(adjacentes(G))

    '''Estados ligados ao estado G'''
    G.addCidadesAdjacentes(adjacentes(H))
    G.addCidadesAdjacentes(adjacentes(L))

    '''Estados ligados ao estado H'''
    H.addCidadesAdjacentes(adjacentes(D))
    
    '''Estados ligados ao estado L'''
    L.addCidadesAdjacentes(adjacentes(M))

    '''Estados ligados ao estado M'''
    M.addCidadesAdjacentes(adjacentes(Q))

    '''Estados ligados ao estado E'''
    E.addCidadesAdjacentes(adjacentes(N))
    E.addCidadesAdjacentes(adjacentes(I))

    '''Estados ligados ao estado I'''
    I.addCidadesAdjacentes(adjacentes(J))

    '''Estados ligados ao estado J'''
    J.addCidadesAdjacentes(adjacentes(O))
    
    '''Estados ligados ao estado O'''
    O.addCidadesAdjacentes(adjacentes(P))
    O.addCidadesAdjacentes(adjacentes(R))

    '''Estados ligados ao estado P'''
    P.addCidadesAdjacentes(adjacentes(Q))

    '''Estados ligados ao estado R'''
    R.addCidadesAdjacentes(adjacentes(S))
    

