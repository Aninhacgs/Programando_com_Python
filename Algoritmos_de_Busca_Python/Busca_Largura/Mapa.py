from MapaCidades import cidade
from Adjacentes import adjacentes

class Mapa:
    portoUniao = cidade("Porto União",203)
    pauloFrontin = cidade("Paulo Frontin",172)
    canoinhas = cidade("canoinhas",141)
    irati = cidade("irati",139)
    palmeira = cidade("palmeira",59)
    campoLargo = cidade("Campo Largo",27)
    curitiba = cidade("Curitiba",0)
    balsaNova = cidade("Balsa Nova",41)
    araucaia = cidade("Araucaia",23)
    saoJose = cidade("São José dos Pinhais",13)
    contenda = cidade("Contenda",39)
    mafra = cidade("Mafra",94)
    tijucas = cidade("Tijucas do Sul",56)
    lapa = cidade("Lapa",74)
    saoMateus = cidade("São Mateus do Sul",123)
    tresBarras = cidade("Três Barras",131)
    
    portoUniao.addCidadesAdjacentes(adjacentes(pauloFrontin))
    portoUniao.addCidadesAdjacentes(adjacentes(canoinhas))
    portoUniao.addCidadesAdjacentes(adjacentes(saoMateus))
    
    pauloFrontin.addCidadesAdjacentes(adjacentes(portoUniao))
    pauloFrontin.addCidadesAdjacentes(adjacentes(irati))
    
    canoinhas.addCidadesAdjacentes(adjacentes(portoUniao))
    canoinhas.addCidadesAdjacentes(adjacentes(tresBarras))
    canoinhas.addCidadesAdjacentes(adjacentes(mafra))
    
    irati.addCidadesAdjacentes(adjacentes(pauloFrontin))
    irati.addCidadesAdjacentes(adjacentes(palmeira))
    irati.addCidadesAdjacentes(adjacentes(saoMateus))
    
    palmeira.addCidadesAdjacentes(adjacentes(irati))
    palmeira.addCidadesAdjacentes(adjacentes(saoMateus))
    palmeira.addCidadesAdjacentes(adjacentes(campoLargo))
    
    campoLargo.addCidadesAdjacentes(adjacentes(palmeira))
    campoLargo.addCidadesAdjacentes(adjacentes(balsaNova))
    campoLargo.addCidadesAdjacentes(adjacentes(curitiba))
    
    curitiba.addCidadesAdjacentes(adjacentes(campoLargo))
    curitiba.addCidadesAdjacentes(adjacentes(balsaNova))
    curitiba.addCidadesAdjacentes(adjacentes(araucaia))
    curitiba.addCidadesAdjacentes(adjacentes(saoJose))
    
    balsaNova.addCidadesAdjacentes(adjacentes(curitiba))
    balsaNova.addCidadesAdjacentes(adjacentes(campoLargo))
    balsaNova.addCidadesAdjacentes(adjacentes(contenda))
    
    araucaia.addCidadesAdjacentes(adjacentes(curitiba))
    araucaia.addCidadesAdjacentes(adjacentes(contenda))
    
    saoJose.addCidadesAdjacentes(adjacentes(curitiba))
    saoJose.addCidadesAdjacentes(adjacentes(tijucas))
    
    contenda.addCidadesAdjacentes(adjacentes(balsaNova))
    contenda.addCidadesAdjacentes(adjacentes(araucaia))
    contenda.addCidadesAdjacentes(adjacentes(lapa))
    
    mafra.addCidadesAdjacentes(adjacentes(tijucas))
    mafra.addCidadesAdjacentes(adjacentes(lapa))
    mafra.addCidadesAdjacentes(adjacentes(canoinhas))
    
    tijucas.addCidadesAdjacentes(adjacentes(mafra))
    tijucas.addCidadesAdjacentes(adjacentes(saoJose))
    
    lapa.addCidadesAdjacentes(adjacentes(contenda))
    lapa.addCidadesAdjacentes(adjacentes(saoMateus))
    lapa.addCidadesAdjacentes(adjacentes(mafra))
    
    saoMateus.addCidadesAdjacentes(adjacentes(palmeira))
    saoMateus.addCidadesAdjacentes(adjacentes(irati))
    saoMateus.addCidadesAdjacentes(adjacentes(tresBarras))
    saoMateus.addCidadesAdjacentes(adjacentes(portoUniao))
    
    tresBarras.addCidadesAdjacentes(adjacentes(saoMateus))
    tresBarras.addCidadesAdjacentes(adjacentes(canoinhas))
    
    
'''mapa = Mapa()

mapa.portoUniao
mapa.portoUniao.visitado
mapa.portoUniao.adjacentes
mapa.portoUniao.distanciaObjetivo

for i in range(len(mapa.portoUniao.adjacentes)):
    print(mapa.portoUniao.adjacentes[i].cidade.nome)'''
