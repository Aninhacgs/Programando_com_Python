class VetorOrdenado:
    def __init__(self,tamanho):
        self.numeroElementos = 0
        self.letras = [None] * tamanho
        
    def inserir(self,Letras):
        if self.numeroElementos == 0:
            self.letras[0] = Letras
            self.numeroElementos = 1
        else:
            self.letras[self.numeroElementos] = Letras
            self.numeroElementos += 1
    
    def mostrar(self):
        print(' \n\n Nó  CUSTO ')
        for i in range(0,self.numeroElementos):
            print('  {}    {}      '.format(self.letras[i].nome,self.letras[i].distancia))

    
    def buscar(self):
        l = input('\nDigite uma letra para buscar no mapa: ')
        busca = l.upper()
        if busca == 'A':
            custo = self.letras[0].distancia
            print('\nA letra ',busca,'foi encontrada na posição 0 com um custo',custo )
            
        elif busca == 'B':
            custo =+ self.letras[1].distancia 
            print('\nA letra ',busca,'foi encontrada na posição 1 com um custo',custo )
            
        elif busca == 'C':
            custo =+ self.letras[1].distancia 
            custo += self.letras[2].distancia
            print('\nA letra ',busca,'foi encontrada na posição 2 com um custo',custo )
            
        elif busca == 'D':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            print('\nA letra ',busca,'foi encontrada na posição 3 com um custo',custo )
            
        elif busca == 'E':
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
            print('\nA letra ',busca,'foi encontrada na posição 12 com um custo',custo )
            
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
            custo += self.letras[13].distancia
            print('\nA letra ',busca,'foi encontrada na posição 13 com um custo',custo )
            
        elif busca == 'G':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            custo += self.letras[5].distancia
            custo += self.letras[6].distancia
            custo += self.letras[7].distancia
            custo += self.letras[8].distancia
            print('\nA letra ',busca,'foi encontrada na posição 8 com um custo',custo )
            
        elif busca == 'H':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            custo += self.letras[5].distancia
            custo += self.letras[6].distancia
            custo += self.letras[7].distancia
            custo += self.letras[8].distancia
            custo += self.letras[9].distancia
            print('\nA letra ',busca,'foi encontrada na posição 9 com um custo',custo )
            
        elif busca == 'J':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            custo += self.letras[5].distancia
            print('\nA letra ',busca,'foi encontrada na posição 5 com um custo',custo )
            
        elif busca == 'K':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            print('\nA letra ',busca,'foi encontrada na posição 4 com um custo',custo )
            
        elif busca == 'M':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            custo += self.letras[5].distancia
            custo += self.letras[6].distancia
            custo += self.letras[7].distancia
            print('\nA letra ',busca,'foi encontrada na posição 7 com um custo',custo )
            
        elif busca == 'L':
            custo =+ self.letras[1].distancia
            custo += self.letras[2].distancia
            custo += self.letras[3].distancia
            custo += self.letras[4].distancia
            custo += self.letras[5].distancia
            custo += self.letras[6].distancia
            print('\nA letra ',busca,'foi encontrada na posição 6 com um custo',custo )
            
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
            print('\nA letra ',busca,'foi encontrada na posição 10 com um custo',custo )
            
        elif busca == 'O':
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
            print('\nA letra ',busca,'foi encontrada na posição 11 com um custo',custo )
            
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
            custo += self.letras[14].distancia
            print('\nA letra ',busca,'foi encontrada na posição 14 com um custo',custo )
            
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
            custo += self.letras[15].distancia
            print('\nA letra ',busca,'foi encontrada na posição 14 com um custo',custo )
            
        else:
            print('\nA letra ',busca,'não pertence ao mapa!')
            
            
            
            


        