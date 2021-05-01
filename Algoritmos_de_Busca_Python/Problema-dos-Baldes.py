#-*- coding:utf-8 -*-

def sucessores( node, caminho ):
    if node == [ -1, -1 ]:
        return [  [0,0,''] , [4,0,'encheu A'] , [0,3, 'encheu B'] ]
    else:
        retorno = []
        # encher o balde A
        if node[0] != 4: retorno.append( [ 4 , node[1] , 'encheu   A' ] )
        # encher o balde B
        if node[1] != 3: retorno.append( [ node[0] , 3 , 'encheu   B' ] )
        # esvaziar o balde A
        if node[0] != 0: retorno.append( [ 0 , node[1] , 'esvaziou A' ] )
        # esvaziar o balde B
        if node[1] != 0: retorno.append( [ node[0] , 0 , 'esvaziou B' ] )
        # despejar balde A em B
        if node[0] != 0 or node[1] != 3:
            qntAgua = 3-node[1]
            if qntAgua > node[0]: qntAgua = node[0] 
            baldeA  = node[0] - qntAgua 
            baldeB  = node[1] + qntAgua 
            retorno.append([ baldeA, baldeB , 'despejou A em B' ])
        # despejar o balde B em A
        if node[1] != 0 or node[0] != 4:
            qntAgua = 4-node[0]
            if qntAgua > node[1]: qntAgua = node[1]
            baldeA  = node[0] + qntAgua 
            baldeB  = node[1] - qntAgua 
            retorno.append([ baldeA, baldeB , 'despejou B em A' ])
        
        for i in caminho:
            try: retorno.remove( i )
            except: pass
        return retorno

def funcaoAvaliacao( node ):
    if node[0] == 2 and node[1] == 0:
        return True
    else:
        return False

from sys import exit

lista  = []
estado = [ -1 , -1, '' ]
caminho = []
print ('Caminhando:')
while True:
    caminho = caminho + [estado]
    if funcaoAvaliacao( estado ):
        print ('\nSucesso, objetivo encontrado:'), estado
        caminho.pop()
        print ('Caminho:')
        for i in caminho: print (i[2])
        exit(0)
    else:
        #profundidade: insere no início da lista
        lista = sucessores( estado , caminho ) + lista
    
    if lista == []:
        print ('\nFALHA, não foi possível encontrar objetivo')
        exit(1)

    estado = lista[0]
    lista.pop(0)
