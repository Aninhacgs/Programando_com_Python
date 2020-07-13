class Letras:
    def __init__(self,nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        
    def addCidadesAdjacentes(self,Letras):
        self.adjacentes.append(Letras)

c = Letras("teste")
c.nome
c.visitado
