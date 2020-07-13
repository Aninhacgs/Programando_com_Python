from Letras import Letras
from Adjacentes import Adjacentes

class Mapa:
    A = Letras("A")
    B = Letras("B")
    C = Letras("C")
    D = Letras("D")
    E = Letras("E")
    F = Letras("F")
    G = Letras("G")
    H = Letras("H")
    J = Letras("J")
    K = Letras("H")
    L = Letras("L")
    M = Letras("M")
    N = Letras("N")
    O = Letras("O")
    R = Letras("R")
    S = Letras("S")
    
    '''Adicionando as letras que são adjacentes a letra A'''
    A.AddLetrasAdjacentes(Adjacentes(B))
    A.AddLetrasAdjacentes(Adjacentes(C))
    A.AddLetrasAdjacentes(Adjacentes(D))
    
    '''Adicionando as letras que são adjacentes a letra B'''
    B.AddLetrasAdjacentes(Adjacentes(K))
    B.AddLetrasAdjacentes(Adjacentes(J))
    
    '''Adicionando as letras que são adjacentes a letra J'''
    J.AddLetrasAdjacentes(Adjacentes(L))
    J.AddLetrasAdjacentes(Adjacentes(M))
    
    '''Adicionando as letras que são adjacentes a letra C'''
    C.AddLetrasAdjacentes(Adjacentes(G))
    C.AddLetrasAdjacentes(Adjacentes(H))
    
    '''Adicionando as letras que são adjacentes a letra G'''
    G.AddLetrasAdjacentes(Adjacentes(N))
    G.AddLetrasAdjacentes(Adjacentes(O))
    
    '''Adicionando as letras que são adjacentes a letra D'''
    D.AddLetrasAdjacentes(Adjacentes(E))
    D.AddLetrasAdjacentes(Adjacentes(F))
    
    '''Adicionando as letras que são adjacentes a letra F'''
    F.AddLetrasAdjacentes(Adjacentes(R))
    F.AddLetrasAdjacentes(Adjacentes(S))
    