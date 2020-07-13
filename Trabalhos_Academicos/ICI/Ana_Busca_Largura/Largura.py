from Fila import Fila

class Largura:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(16)
        self.fronteira.enfileirar(inicio)
        self.achou = False
        
    def buscar(self):
        primeiro = self.fronteira.getPrimeiro()
        print('Primeiro elemento da lista'.format(primeiro.nome))
        
        if primeiro == self.objetivo:
            self.achou = True
        else:
            temp = self.fronteira.desenfileirar()
            print('Desenfileirou {}'.format(temp.nome))
            
            for a in primeiro.adjacentes:
                print('Verificando se já foi visitado: {}'.format(a.letras.nome))
                if a.letras.visitado == False:
                    a.letras.visitado = True
                    self.fronteira.enfileirar(a.letras)
            if self.fronteira.numerosElementos > 0:
                Largura.buscar(self)
                
from Mapa import Mapa
mapa = Mapa()
largura = Largura(mapa.A,mapa.H)
largura.buscar()




