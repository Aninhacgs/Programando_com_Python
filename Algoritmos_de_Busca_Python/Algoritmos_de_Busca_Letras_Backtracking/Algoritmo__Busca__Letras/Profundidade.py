'''Verifica todos os valores e os empilha em uma pilha até encontrar o valor da variável objetivo
depois começa o processo de desempilhar'''

from Pilha import Pilha

class Backtracking:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        print('Topo: {}'.format(topo.nome))
        
        if topo == self.objetivo:
            self.achou = True
        else:
            '''For para percorrer todos os vertices do topo'''
        
            for a in topo.adjacentes:
                if self.achou == False:
                    print('Estado a ser visitado: {}'.format(a.Letras.nome))
                    if a.Letras.visitado == False:
                        a.Letras.visitado = True
                        self.fronteira.empilhar(a.Letras)
                        Backtracking.buscar(self)
                
        print('Desempilhou: {}'.format(self.fronteira.desempilhar().nome))
        

from Mapa import Mapa
mapa = Mapa()

backtracking = Backtracking(mapa.A,mapa.S)
backtracking.buscar()
