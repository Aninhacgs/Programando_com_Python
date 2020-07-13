class Letras:
    def __init__(self,nome,distancia):
        self.nome = nome
        self.distancia = distancia
        self.visitado = False
        self.adjacentes = []
        
    def AddLetrasAdjacentes(self,letras):
        self.adjacentes.append(letras)