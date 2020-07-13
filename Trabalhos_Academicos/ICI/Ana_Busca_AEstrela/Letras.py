class Letras:
    def __init__(self,nome,distancia,estimativa):
        self.nome = nome
        self.distancia = distancia
        self.estimativa = estimativa
        self.visitado = False
        self.adjacentes = []
        
    def AddLetrasAdjacentes(self,letras):
        self.adjacentes.append(letras)