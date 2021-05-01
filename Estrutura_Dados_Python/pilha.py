class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0

pilha = Pilha()
print(pilha.vazia())
pilha.empilha(1)
pilha.empilha(2)
pilha.empilha(3)
print(pilha.vazia())
print(pilha.desempilha())
print(pilha.desempilha())
print(pilha.desempilha())
print(pilha.vazia())
