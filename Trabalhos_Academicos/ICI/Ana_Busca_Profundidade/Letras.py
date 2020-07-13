class Letras:
    def __init__(self,nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        
    def AddLetrasAdjacentes(self,letras):
        self.adjacentes.append(letras)
        
        
        
        