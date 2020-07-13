from MapaCidades import cidade
from Adjacentes import adjacentes

class Mapa:
    portoUniao = cidade("Porto União")
    pauloFrontin = cidade("Paulo Frontin")
    canoinhas = cidade("canoinhas")
    irati = cidade("irati")
    palmeira = cidade("palmeira")
    campoLargo = cidade("Campo Largo")
    curitiba = cidade("Curitiba")
    balsaNova = cidade("Balsa Nova")
    araucaia = cidade("Araucaia")
    saoJose = cidade("São José dos Pinhais")
    contenda = cidade("Contenda")
    mafra = cidade("Mafra")
    tijucas = cidade("Tijucas do Sul")
    lapa = cidade("Lapa")
    saoMateus = cidade("São Mateus do Sul")
    tresBarras = cidade("Três Barras")
    
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

for i in range(len(mapa.portoUniao.adjacentes)):
    print(mapa.portoUniao.adjacentes[i].cidade.nome)'''
