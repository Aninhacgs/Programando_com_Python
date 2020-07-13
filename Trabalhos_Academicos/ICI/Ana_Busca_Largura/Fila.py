class Fila:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.letras = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numerosElementos = 0
        
    def enfileirar(self, letras):
        if not Fila.filaCheia(self):
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim +=1 
            self.letras[self.fim] = letras
            self.numerosElementos += 1
            
        else:
            print('A fila está cheia!')
        
        
    def desenfileirar(self):
        if not Fila.filaVazia(self):
            temp = self.letras[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numerosElementos -= 1
            return temp
        else:
            print('A fila já está vazia!')
            return None
        
    def getPrimeiro(self):
        return self.letras[self.inicio]
    
    
    def filaVazia(self):
        return self.numerosElementos == 0
    
    def filaCheia(self):
        return self.numerosElementos == self.tamanho


