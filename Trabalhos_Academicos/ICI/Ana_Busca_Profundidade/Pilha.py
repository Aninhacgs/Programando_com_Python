class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.letras = [None] * self.tamanho
        self.topo = -1
        
    def empilhar(self,letras):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.letras[self.topo] = letras
        else:
            print('A pilha está cheia!')
        
    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.letras[self.topo]
            self.topo -= 1
            return temp
        else:
            print('A pilha já está vazia!')
            return None
        
    def getTopo(self):
        return self.letras[self.topo]
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return (self.topo == self.tamanho -1)
    
    
    