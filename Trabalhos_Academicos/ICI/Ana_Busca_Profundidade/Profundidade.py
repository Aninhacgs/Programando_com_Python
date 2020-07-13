from Pilha import Pilha

class Profundidade:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(16)
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        print('Topo {}'.format(topo.nome))
        
        if topo == self.objetivo:
            self.achou = True
            return print('A letra {}'.format(topo.nome)+' foi encontrada!')
        else:
            for a in topo.adjacentes:
                if self.achou == False:
                    if a.letras.visitado == False:
                        a.letras.visitado = True
                        print('Estado visitado: {}'.format(a.letras.nome))
                        self.fronteira.empilhar(a.letras)
                        Profundidade.buscar(self)
            print('Desempilhou: {}'.format(self.fronteira.desempilhar().nome))

from Mapa import Mapa
mapa = Mapa()

profundidade = Profundidade(mapa.A,mapa.C)
profundidade.buscar()



