class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.Letras = [None] * self.tamanho
        self.topo = -1
        
    def empilhar(self,Letras):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.Letras[self.topo] = Letras
        else:
            print("A pilha já está cheia!")
            
        
    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.Letras[self.topo]
            self.topo -= 1
            return temp
        else:
            print("A pilha já está vazia!")
            return None
    
    def getTopo(self):
        return self.Letras[self.topo]
    
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return(self.topo == self.tamanho - 1)
        

from Mapa import Mapa

mapa = Mapa()
p = Pilha(5)
p.empilhar(mapa.A)
p.empilhar(mapa.B)
p.empilhar(mapa.E)

p.getTopo().nome

