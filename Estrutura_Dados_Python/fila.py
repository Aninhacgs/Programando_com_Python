class Fila(object):
    def __init__(self):
        self.dados = []
 
    def insere(self, elemento):
        self.dados.append(elemento)
 
    def retira(self):
        return self.dados.pop(0)
 
    def vazia(self):
        return len(self.dados) == 0

fila = Fila()
fila.insere(1)
fila.insere(2)
fila.insere(3)
print(fila.vazia())
print(fila.retira())
print(fila.retira())
print(fila.retira())
print(fila.vazia())



