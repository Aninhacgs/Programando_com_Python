class cidade:
    def __init__(self,nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        
    def addCidadesAdjacentes(self,cidade):
        self.adjacentes.append(cidade)

c = cidade("teste")
c.nome
c.visitado