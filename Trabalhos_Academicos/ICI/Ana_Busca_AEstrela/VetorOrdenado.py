class VetorOrdenado:
    def __init__(self,tamanho):
        self.numeroElementos = 0
        self.letras = [None] * tamanho
        
    def inserir(self,Letras):
        if self.numeroElementos == 0:
            self.letras[0] = Letras
            self.numeroElementos = 1
            return
        posicao = 0
        i = 0
        
        while i < self.numeroElementos:
            if Letras.estimativa > self.letras[posicao].estimativa:
                posicao += 1
            i += 1
        
        for k in range(self.numeroElementos,posicao,-1):
            self.letras[k] = self.letras[k - 1]
            
        self.letras[posicao] = Letras
        self.numeroElementos += 1
    
    def mostrar(self):
        print('\n\n  Nó   ESTIMATIVA   CUSTO')
        for i in range(0,self.numeroElementos):
            print('  {}       {}           {}'.format(self.letras[i].nome,self.letras[i].estimativa,self.letras[i].distancia))
            
            
    def buscar(self):
        l = input('Digite a letra para buscar no mapa: ')
        busca = l.upper()
        if busca == 'A':
            custo = self.letras[0].distancia
            estimativa = self.letras[0].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 0!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'B':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia
            estimativa =+ self.letras[1].estimativa 
            estimativa += self.letras[2].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 2!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'C':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia 
            custo += self.letras[3].distancia 
            custo += self.letras[4].distancia 
            custo += self.letras[5].distancia
            estimativa =+ self.letras[1].estimativa 
            estimativa += self.letras[2].estimativa 
            estimativa += self.letras[3].estimativa 
            estimativa += self.letras[4].estimativa 
            estimativa += self.letras[5].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 5!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'D':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia 
             custo += self.letras[11].distancia
             custo += self.letras[12].distancia 
             custo += self.letras[13].distancia 
             custo += self.letras[14].distancia 
             custo += self.letras[15].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa 
             estimativa += self.letras[11].estimativa
             estimativa += self.letras[12].estimativa 
             estimativa += self.letras[13].estimativa 
             estimativa += self.letras[14].estimativa 
             estimativa += self.letras[15].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 15!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao) 

        
        elif busca == 'E':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia 
            custo += self.letras[3].distancia 
            custo += self.letras[4].distancia
            estimativa =+ self.letras[1].estimativa 
            estimativa += self.letras[2].estimativa 
            estimativa += self.letras[3].estimativa 
            estimativa += self.letras[4].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 4!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'F':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia 
             custo += self.letras[11].distancia
             custo += self.letras[12].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa 
             estimativa += self.letras[11].estimativa
             estimativa += self.letras[12].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 12!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)  
        
        elif busca == 'G':
            custo = self.letras[1].distancia
            estimativa = self.letras[1].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 1!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'H':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia 
            custo += self.letras[3].distancia 
            custo += self.letras[4].distancia 
            custo += self.letras[5].distancia
            custo += self.letras[6].distancia
            estimativa =+ self.letras[1].estimativa 
            estimativa += self.letras[2].estimativa 
            estimativa += self.letras[3].estimativa 
            estimativa += self.letras[4].estimativa 
            estimativa += self.letras[5].estimativa 
            estimativa += self.letras[6].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 6!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'J':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia 
             custo += self.letras[11].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa 
             estimativa += self.letras[11].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 11!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)     
        
        elif busca == 'K':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 7!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
             
        elif busca == 'L':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 9!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao) 
        
        elif busca == 'M':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 8!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
        
        elif busca == 'N':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 10!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao) 
        
        elif busca == 'O':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia 
            custo += self.letras[3].distancia
            estimativa =+ self.letras[1].estimativa 
            estimativa += self.letras[2].estimativa 
            estimativa += self.letras[3].estimativa
            funcaoAvaliacao = custo + estimativa
            print('Letra encontrada na posição 3!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
            
        elif busca == 'R':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia 
             custo += self.letras[11].distancia 
             custo += self.letras[12].distancia 
             custo += self.letras[13].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa 
             estimativa += self.letras[11].estimativa
             estimativa += self.letras[12].estimativa 
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 13!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao)
             
        elif busca == 'S':
             custo =+ self.letras[1].distancia 
             custo += self.letras[2].distancia 
             custo += self.letras[3].distancia 
             custo += self.letras[4].distancia 
             custo += self.letras[5].distancia
             custo += self.letras[6].distancia 
             custo += self.letras[7].distancia 
             custo += self.letras[8].distancia 
             custo += self.letras[9].distancia 
             custo += self.letras[10].distancia 
             custo += self.letras[11].distancia
             custo += self.letras[12].distancia 
             custo += self.letras[13].distancia 
             custo += self.letras[14].distancia
             estimativa =+ self.letras[1].estimativa 
             estimativa += self.letras[2].estimativa 
             estimativa += self.letras[3].estimativa 
             estimativa += self.letras[4].estimativa 
             estimativa += self.letras[5].estimativa 
             estimativa += self.letras[6].estimativa 
             estimativa += self.letras[7].estimativa 
             estimativa += self.letras[8].estimativa 
             estimativa += self.letras[9].estimativa 
             estimativa += self.letras[10].estimativa 
             estimativa += self.letras[11].estimativa
             estimativa += self.letras[12].estimativa 
             estimativa += self.letras[13].estimativa 
             estimativa += self.letras[14].estimativa
             funcaoAvaliacao = custo + estimativa
             print('Letra encontrada na posição 14!\nValor do custo = ',custo,'\nValor da estimativa = ',estimativa,
                  '\nValor função avaliação = ',funcaoAvaliacao) 
             
        else:
            print('A letra',busca,'não pertence ao mapa!')


        