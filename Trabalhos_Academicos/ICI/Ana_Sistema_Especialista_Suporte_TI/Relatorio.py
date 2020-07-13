import numpy as np

from BaseConhecimento import Conhecimento
base = Conhecimento

class Resposta:
    def getRespostas():
        respostas= np.matrix([[0,0,0,0,0,0,0,0,0,0,0]])
        
        print('==========SUPORTE TI==========\n')
        print('1 - Computador liga normalmente, mas não inicaliza o sistema operacional com exito\n')
        print('2 - Problemas com o monitor\n')
        print('3 - Os LEDs se acendem, mas o computador não inicia ou reinicia e exibe uma tela preta\n')
        
        
        
        respostas[0,0] = int(input('\nDigite um valor para selecionar a opção: '))
        
        while (respostas[0,0] != 1 and respostas[0,0] != 2 and respostas[0,0] != 3):
            respostas[0,0] = int(input('Opção de menu incorreta!Por favor digite novamente: '))
        
        if respostas[0,0] == 1:
            print('\n\n\nPara as perguntas abaixo digite 1 para sim e 0 para não\n')
            respostas[0,1] = int(input('O sistema liga? '))
            while(respostas[0,1] != 1 and respostas[0,1] != 0):
                respostas[0,1] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,2] = int(input('Tem vídeo,mas o sistema operacional não termina o boot? '))
            while(respostas[0,2] != 1 and respostas[0,2] != 0):
                respostas[0,2] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,3] = int(input('A tecla Caps Look é acessa quando ativada? '))
            while(respostas[0,3] != 1 and respostas[0,3] != 0):
                respostas[0,3] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,4] = int(input('O indicador de atividade do disco rígido está piscando? '))
            while(respostas[0,4] != 1 and respostas[0,4] != 0):
                respostas[0,4] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,5] = int(input('O indicador de atividade do disco rígido está acesso? '))
            while(respostas[0,5] != 1 and respostas[0,5] != 0):
                respostas[0,5] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,6] = int(input('O indicador de atividade do disco rígido está apagado? '))
            while(respostas[0,6] != 1 and respostas[0,6] != 0):
                respostas[0,6] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,7] = int(input('Existe uma mensagem de erro na tela? '))
            while(respostas[0,7] != 1 and respostas[0,7] != 0):
                respostas[0,7] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,8] = int(input('Os sons do sistema operacional não são ouvidos? '))
            while(respostas[0,8] != 1 and respostas[0,8] != 0):
                respostas[0,8] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,9] = int(input('O botão liga/desliga fica acesso continuamente em sua cor de operação normal? '))
            while(respostas[0,9] != 1 and respostas[0,9] != 0):
                respostas[0,9] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,10] = int(input('Existe códigos de diagnóstico? '))
            while(respostas[0,10] != 1 and respostas[0,10] != 0):
                respostas[0,10] = int(input('Opção incorreta! Digite novamente: '))
        
        elif respostas[0,0] == 2:
            print('\n\n\nPara as perguntas abaixo digite 1 para sim e 0 para não\n')
            respostas[0,1] = int(input('A imagem na tela apresenta texto confuso? '))
            while(respostas[0,1] != 1 and respostas[0,1] != 0):
                respostas[0,1] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,2] = int(input('A imagem na tela está desfocada? '))
            while(respostas[0,2] != 1 and respostas[0,2] != 0):
                respostas[0,2] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,3] = int(input('A imagem na tela está esticada? '))
            while(respostas[0,3] != 1 and respostas[0,3] != 0):
                respostas[0,3] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,4] = int(input('A imagem na tela apresenta pequenos pontos claros ou escuros? '))
            while(respostas[0,4] != 1 and respostas[0,4] != 0):
                respostas[0,4] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,5] = int(input('A imagem na tela encolhe ao conectar um monitor externo? '))
            while(respostas[0,5] != 1 and respostas[0,5] != 0):
                respostas[0,5] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,6] = int(input('Normalmente, a imagem na tela é nítida, mas fica distorcida? '))
            while(respostas[0,6] != 1 and respostas[0,6] != 0):
                respostas[0,6] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,7] = int(input('A imagem na tela apresenta várias linhas horizontais e verticais irregulares? '))
            while(respostas[0,7] != 1 and respostas[0,7] != 0):
                respostas[0,7] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,8] = int(input('A imagem na tela apresenta grandes áreas brancas ou pretas? '))
            while(respostas[0,8] != 1 and respostas[0,8] != 0):
                respostas[0,8] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,9] = int(input('A imagem na tela aparece cortada ao executar um programa com altos requisitos gráficos? '))
            while(respostas[0,9] != 1 and respostas[0,9] != 0):
                respostas[0,9] = int(input('Opção incorreta! Digite novamente: '))
            respostas[0,10] = int(input('Não há imagem na tela, ou a tela não mostra nada? '))
            while(respostas[0,10] != 1 and respostas[0,10] != 0):
                respostas[0,10] = int(input('Opção incorreta! Digite novamente: '))
        
        elif respostas[0,0] == 3:
           print('\n\n\nPara as perguntas abaixo digite 1 para sim e 0 para não\n')
           respostas[0,1] = int(input('Os LEDs não acendem, a tela fica preta e o computador não inicia? '))
           while(respostas[0,1] != 1 and respostas[0,1] != 0):
                respostas[0,1] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,2] = int(input('Os LEDs piscam, mas não se inicia? '))
           while(respostas[0,2] != 1 and respostas[0,2] != 0):
                respostas[0,2] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,3] = int(input('O computador emite bipes, mas não se inicia? '))
           while(respostas[0,3] != 1 and respostas[0,3] != 0):
                respostas[0,3] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,4] = int(input('os LEDs acendem, o som da ventoinha é ouvido, mas a tela fica preta ou sem imagem? '))
           while(respostas[0,4] != 1 and respostas[0,4] != 0):
                respostas[0,4] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,5] = int(input('A mensagem de erro é exibida em uma tela preta? '))
           while(respostas[0,5] != 1 and respostas[0,5] != 0):
                respostas[0,5] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,6] = int(input('Uma mensagem de erro é exibida em uma tela azul? '))
           while(respostas[0,6] != 1 and respostas[0,6] != 0):
                respostas[0,6] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,7] = int(input('Exibe o logotipo do Windows na tela e trava? '))
           while(respostas[0,7] != 1 and respostas[0,7] != 0):
                respostas[0,7] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,8] = int(input('O computador inicia após ter carregado o sistema operacional? '))
           while(respostas[0,8] != 1 and respostas[0,8] != 0):
                respostas[0,8] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,9] = int(input('O computador não inicia? '))
           while(respostas[0,9] != 1 and respostas[0,9] != 0):
                respostas[0,9] = int(input('Opção incorreta! Digite novamente: '))
           respostas[0,10] = int(input('O computador pode se reiniciar ou congelar em uma tela azul, sem nenhuma mensagem? '))
           while(respostas[0,10] != 1 and respostas[0,10] != 0):
                respostas[0,10] = int(input('Opção incorreta! Digite novamente: '))
            
        print('\n\n\n==========RELATORIO FINAL==========\n')  
        
        if (base.conhecimento[0,0] == respostas[0,0] and base.conhecimento[0,1] == respostas[0,1] 
            and base.conhecimento[0,2] == respostas[0,2] and base.conhecimento[0,3] == respostas[0,3] 
            and base.conhecimento[0,4] == respostas[0,4] and base.conhecimento[0,5] == respostas[0,5] 
            and base.conhecimento[0,6] == respostas[0,6] and base.conhecimento[0,7] == respostas[0,7] 
            and base.conhecimento[0,8] == respostas[0,8] and base.conhecimento[0,9] == respostas[0,9] 
            and base.conhecimento[0,10] == respostas[0,10]):
            
            print('O computador apresenta um problema de boot e inicialização.\n Verifique se o computador finaliza a inicialização',
                  'inicial (POST), desconecte todos os dispositivos externos e executar uma reinicialização forçada executa e o', 
                  'diagnóstico do computador, verifique se há mensagens de erro específicas, redefina os valores padrão do BIOS',
                   'Reinicie seu sistema operacional e restaure as configurações padrão de fábrica do sistema operacional')
            
        elif(base.conhecimento[1,0] == respostas[0,0] and base.conhecimento[1,1] == respostas[0,1] 
            and base.conhecimento[1,2] == respostas[0,2] and base.conhecimento[1,3] == respostas[0,3] 
            and base.conhecimento[1,4] == respostas[0,4] and base.conhecimento[1,5] == respostas[0,5] 
            and base.conhecimento[1,6] == respostas[0,6] and base.conhecimento[1,7] == respostas[0,7] 
            and base.conhecimento[1,8] == respostas[0,8] and base.conhecimento[1,9] == respostas[0,9] 
            and base.conhecimento[1,10] == respostas[0,10]):
            
             print('O computador apresenta um problema de boot e inicialização.\n Verifique se o computador finaliza a inicialização',
                  'inicial (POST), desconecte todos os dispositivos externos e executar uma reinicialização forçada executa e o', 
                  'diagnóstico do computador, verifique se há mensagens de erro específicas, redefina os valores padrão do BIOS',
                   'Reinicie seu sistema operacional e restaure as configurações padrão de fábrica do sistema operacional')
            
        elif(base.conhecimento[2,0] == respostas[0,0] and base.conhecimento[2,1] == respostas[0,1] 
            and base.conhecimento[2,2] == respostas[0,2] and base.conhecimento[2,3] == respostas[0,3]
            and base.conhecimento[2,4] == respostas[0,4] and base.conhecimento[2,5] == respostas[0,5] 
            and base.conhecimento[2,6] == respostas[0,6] and base.conhecimento[2,7] == respostas[0,7] 
            and base.conhecimento[2,8] == respostas[0,8] and base.conhecimento[2,9] == respostas[0,9] 
            and base.conhecimento[2,10] == respostas[0,10]):
             print('O computador apresenta um problema de boot e inicialização.\n Verifique se o computador finaliza a inicialização',
                  'inicial (POST), desconecte todos os dispositivos externos e executar uma reinicialização forçada executa e o', 
                  'diagnóstico do computador, verifique se há mensagens de erro específicas, redefina os valores padrão do BIOS',
                   'Reinicie seu sistema operacional e restaure as configurações padrão de fábrica do sistema operacional')
            
        elif(base.conhecimento[3,0] == respostas[0,0] and base.conhecimento[3,1] == respostas[0,1] 
            and base.conhecimento[3,2] == respostas[0,2] and base.conhecimento[3,3] == respostas[0,3]
            and base.conhecimento[3,4] == respostas[0,4] and base.conhecimento[3,5] == respostas[0,5] 
            and base.conhecimento[3,6] == respostas[0,6] and base.conhecimento[3,7] == respostas[0,7] 
            and base.conhecimento[3,8] == respostas[0,8] and base.conhecimento[3,9] == respostas[0,9] 
            and base.conhecimento[3,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[4,0] == respostas[0,0] and base.conhecimento[4,1] == respostas[0,1] 
            and base.conhecimento[4,2] == respostas[0,2] and base.conhecimento[4,3] == respostas[0,3]
            and base.conhecimento[4,4] == respostas[0,4] and base.conhecimento[4,5] == respostas[0,5] 
            and base.conhecimento[4,6] == respostas[0,6] and base.conhecimento[4,7] == respostas[0,7] 
            and base.conhecimento[4,8] == respostas[0,8] and base.conhecimento[4,9] == respostas[0,9] 
            and base.conhecimento[4,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[5,0] == respostas[0,0] and base.conhecimento[5,1] == respostas[0,1] 
            and base.conhecimento[5,2] == respostas[0,2] and base.conhecimento[5,3] == respostas[0,3]
            and base.conhecimento[5,4] == respostas[0,4] and base.conhecimento[5,5] == respostas[0,5] 
            and base.conhecimento[5,6] == respostas[0,6] and base.conhecimento[5,7] == respostas[0,7] 
            and base.conhecimento[5,8] == respostas[0,8] and base.conhecimento[5,9] == respostas[0,9] 
            and base.conhecimento[5,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[6,0] == respostas[0,0] and base.conhecimento[6,1] == respostas[0,1] 
            and base.conhecimento[6,2] == respostas[0,2] and base.conhecimento[6,3] == respostas[0,3]
            and base.conhecimento[6,4] == respostas[0,4] and base.conhecimento[6,5] == respostas[0,5] 
            and base.conhecimento[6,6] == respostas[0,6] and base.conhecimento[6,7] == respostas[0,7] 
            and base.conhecimento[6,8] == respostas[0,8] and base.conhecimento[6,9] == respostas[0,9] 
            and base.conhecimento[6,10] == respostas[0,10]):
           print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[7,0] == respostas[0,0] and base.conhecimento[7,1] == respostas[0,1] 
            and base.conhecimento[7,2] == respostas[0,2] and base.conhecimento[7,3] == respostas[0,3]
            and base.conhecimento[7,4] == respostas[0,4] and base.conhecimento[7,5] == respostas[0,5] 
            and base.conhecimento[7,6] == respostas[0,6] and base.conhecimento[7,7] == respostas[0,7] 
            and base.conhecimento[7,8] == respostas[0,8] and base.conhecimento[7,9] == respostas[0,9] 
            and base.conhecimento[7,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[8,0] == respostas[0,0] and base.conhecimento[8,1] == respostas[0,1] 
            and base.conhecimento[8,2] == respostas[0,2] and base.conhecimento[8,3] == respostas[0,3]
            and base.conhecimento[8,4] == respostas[0,4] and base.conhecimento[8,5] == respostas[0,5] 
            and base.conhecimento[8,6] == respostas[0,6] and base.conhecimento[8,7] == respostas[0,7] 
            and base.conhecimento[8,8] == respostas[0,8] and base.conhecimento[8,9] == respostas[0,9] 
            and base.conhecimento[8,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[9,0] == respostas[0,0] and base.conhecimento[9,1] == respostas[0,1] 
            and base.conhecimento[9,2] == respostas[0,2] and base.conhecimento[9,3] == respostas[0,3]
            and base.conhecimento[9,4] == respostas[0,4] and base.conhecimento[9,5] == respostas[0,5] 
            and base.conhecimento[9,6] == respostas[0,6] and base.conhecimento[9,7] == respostas[0,7] 
            and base.conhecimento[9,8] == respostas[0,8] and base.conhecimento[9,9] == respostas[0,9] 
            and base.conhecimento[9,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[10,0] == respostas[0,0] and base.conhecimento[10,1] == respostas[0,1] 
            and base.conhecimento[10,2] == respostas[0,2] and base.conhecimento[10,3] == respostas[0,3]
            and base.conhecimento[10,4] == respostas[0,4] and base.conhecimento[10,5] == respostas[0,5] 
            and base.conhecimento[10,6] == respostas[0,6] and base.conhecimento[10,7] == respostas[0,7] 
            and base.conhecimento[10,8] == respostas[0,8] and base.conhecimento[10,9] == respostas[0,9] 
            and base.conhecimento[10,10] == respostas[0,10]):
            print('Este problema ocorre devido a resolução incorreta da tela, configurações',
                  'incorretas do drive de vídeo e drives da BIOS e de vídeo desatualizados.',
                  'Para resolver este problema reinicie o computador, caso o problema persista',
                  'ajuste a resolução da tela, caso o problema persista atualize o software do driver de vídeo',
                  'e se mesmo assim não conseguir resolver baixe e instale o BIOS e drivers de vídeo mais recentes')
            
        elif(base.conhecimento[11,0] == respostas[0,0] and base.conhecimento[11,1] == respostas[0,1] 
            and base.conhecimento[11,2] == respostas[0,2] and base.conhecimento[11,3] == respostas[0,3]
            and base.conhecimento[11,4] == respostas[0,4] and base.conhecimento[11,5] == respostas[0,5] 
            and base.conhecimento[11,6] == respostas[0,6] and base.conhecimento[11,7] == respostas[0,7] 
            and base.conhecimento[11,8] == respostas[0,8] and base.conhecimento[11,9] == respostas[0,9] 
            and base.conhecimento[11,10] == respostas[0,10]):
            print('Por conta da natureza da tecnologia LCD, um determinado número de pontos (pixels) pode não ser exibido',
                  'corretamente. Se o monitor tiver muitos defeitos de pixels em uma determinada área, as falhas podem', 
                  'obstruir a visualização apropriada das imagens na tela.Instale os drivers atualizados de gráficos e do BIOS', 
                  'para eliminar qualquer possível problema de exibição de software')
            
        elif(base.conhecimento[12,0] == respostas[0,0] and base.conhecimento[12,1] == respostas[0,1] 
            and base.conhecimento[12,2] == respostas[0,2] and base.conhecimento[12,3] == respostas[0,3]
            and base.conhecimento[12,4] == respostas[0,4] and base.conhecimento[12,5] == respostas[0,5] 
            and base.conhecimento[12,6] == respostas[0,6] and base.conhecimento[12,7] == respostas[0,7] 
            and base.conhecimento[12,8] == respostas[0,8] and base.conhecimento[12,9] == respostas[0,9] 
            and base.conhecimento[12,10] == respostas[0,10]):
            print('Esse problema pode ocorrer quando a resolução nativa do computador e a resolução do monitor externo não', 
                  'forem iguais. Quando o controle de vídeo detecta duas telas, ele normalmente usa como padrão a resolução', 
                  'menor para ambos os dispositivos. Para resolver esse problema, desconecte o monitor externo, para verificar',
                  'se a resolução na tela do computador volta para as configurações desejadas. Reconecte o monitor externo e ',
                  'ajuste as configurações de resolução para cada dispositivo usando um dos métodos')
        
        elif(base.conhecimento[13,0] == respostas[0,0] and base.conhecimento[13,1] == respostas[0,1] 
            and base.conhecimento[13,2] == respostas[0,2] and base.conhecimento[13,3] == respostas[0,3]
            and base.conhecimento[13,4] == respostas[0,4] and base.conhecimento[13,5] == respostas[0,5] 
            and base.conhecimento[13,6] == respostas[0,6] and base.conhecimento[13,7] == respostas[0,7] 
            and base.conhecimento[13,8] == respostas[0,8] and base.conhecimento[13,9] == respostas[0,9] 
            and base.conhecimento[13,10] == respostas[0,10]):
            print('Este problema ocorre devido a desatualização de drives, ajustes incorretos da resolução de vídeo e ajustes',
                  'incorretos da resolução de jogos eletrônicos. Para resolver este problema Certifique-se de que a resolução de',
                  'vídeo corresponda à resolução do programa,Consulte a documentação do fabricante do software para obter informações', 
                  'sobre como ajustar a resolução do jogo e instale atualizações de drivers gráficos')
            
        elif(base.conhecimento[14,0] == respostas[0,0] and base.conhecimento[14,1] == respostas[0,1] 
            and base.conhecimento[14,2] == respostas[0,2] and base.conhecimento[14,3] == respostas[0,3]
            and base.conhecimento[14,4] == respostas[0,4] and base.conhecimento[14,5] == respostas[0,5] 
            and base.conhecimento[14,6] == respostas[0,6] and base.conhecimento[14,7] == respostas[0,7] 
            and base.conhecimento[14,8] == respostas[0,8] and base.conhecimento[14,9] == respostas[0,9] 
            and base.conhecimento[14,10] == respostas[0,10]):
            print('Uma tela LCD rachada indica danos em inúmeros padrões diferentes. Esse tipo de dano físico pode ser detectado já nas', 
                  'operações de inicialização, em nível de BIOS, antes do computador entrar no Windows (ou outros sistemas operacionais).', 
                  'A tela deve ser substituída. Não há nenhuma ação disponível para corrigir esse problema. O computador pode ser', 
                  'utilizado quando conectado a um monitor externo.')
            
        elif(base.conhecimento[15,0] == respostas[0,0] and base.conhecimento[15,1] == respostas[0,1] 
            and base.conhecimento[15,2] == respostas[0,2] and base.conhecimento[15,3] == respostas[0,3]
            and base.conhecimento[15,4] == respostas[0,4] and base.conhecimento[15,5] == respostas[0,5] 
            and base.conhecimento[15,6] == respostas[0,6] and base.conhecimento[15,7] == respostas[0,7] 
            and base.conhecimento[15,8] == respostas[0,8] and base.conhecimento[15,9] == respostas[0,9] 
            and base.conhecimento[15,10] == respostas[0,10]):
            print('Uma tela LCD rachada indica danos em inúmeros padrões diferentes. Esse tipo de dano físico pode ser detectado já nas', 
                  'operações de inicialização, em nível de BIOS, antes do computador entrar no Windows (ou outros sistemas operacionais).', 
                  'A tela deve ser substituída. Não há nenhuma ação disponível para corrigir esse problema. O computador pode ser', 
                  'utilizado quando conectado a um monitor externo.')
        
        elif(base.conhecimento[16,0] == respostas[0,0] and base.conhecimento[16,1] == respostas[0,1] 
            and base.conhecimento[16,2] == respostas[0,2] and base.conhecimento[16,3] == respostas[0,3]
            and base.conhecimento[16,4] == respostas[0,4] and base.conhecimento[16,5] == respostas[0,5] 
            and base.conhecimento[16,6] == respostas[0,6] and base.conhecimento[16,7] == respostas[0,7] 
            and base.conhecimento[16,8] == respostas[0,8] and base.conhecimento[16,9] == respostas[0,9] 
            and base.conhecimento[16,10] == respostas[0,10]):
            print('Este problema ocorre devido a desatualização de drives, ajustes incorretos da resolução de vídeo e ajustes',
                  'incorretos da resolução de jogos eletrônicos. Para resolver este problema Certifique-se de que a resolução de',
                  'vídeo corresponda à resolução do programa,Consulte a documentação do fabricante do software para obter informações', 
                  'sobre como ajustar a resolução do jogo e instale atualuzação de drivers gráficos')
        
        elif(base.conhecimento[17,0] == respostas[0,0] and base.conhecimento[17,1] == respostas[0,1] 
            and base.conhecimento[17,2] == respostas[0,2] and base.conhecimento[17,3] == respostas[0,3]
            and base.conhecimento[17,4] == respostas[0,4] and base.conhecimento[17,5] == respostas[0,5] 
            and base.conhecimento[17,6] == respostas[0,6] and base.conhecimento[17,7] == respostas[0,7] 
            and base.conhecimento[17,8] == respostas[0,8] and base.conhecimento[17,9] == respostas[0,9] 
            and base.conhecimento[17,10] == respostas[0,10]):
            print('Se a tela do notebook continuar preta ou não mostrar imagem, e não for exibida nenhuma mensagem de erro', 
                  'nela, você deverá determinar se essa condição é causada por um problema na tela ou se indica um problema',
                  'na inicialização do computador\nPara testar se a tela está com defeito, siga as etapas abaixo:\n',
                  'Conecte o computador a um monitor externo usando um cabo conector VGA ou HDMI.\n',
                  'Conecte a alimentação CA ao computador e ao monitor externo.\n',
                  'Pressione o botão Liga/Desliga no computador e pressione o botão Liga/Desliga no monitor externo.\n'
                  'Se uma imagem for exibida no monitor externo, mas não na tela do computador, baixe e instale o BIOS',
                  'mais recente, o driver gráfico mais recente, assim como o chipset mais recente da CPU. Consulte o',
                  'documento de suporte Obter software e drivers para mais informações.\n',
                  'Se não for exibida nenhuma imagem na tela do computador, nem no monitor externo, e o computador não se', 
                  'inicializar adequadamente, isso indica um problema de inicialização, e não com a tela')
            
        elif(base.conhecimento[18,0] == respostas[0,0] and base.conhecimento[18,1] == respostas[0,1] 
            and base.conhecimento[18,2] == respostas[0,2] and base.conhecimento[18,3] == respostas[0,3]
            and base.conhecimento[18,4] == respostas[0,4] and base.conhecimento[18,5] == respostas[0,5] 
            and base.conhecimento[18,6] == respostas[0,6] and base.conhecimento[18,7] == respostas[0,7] 
            and base.conhecimento[18,8] == respostas[0,8] and base.conhecimento[18,9] == respostas[0,9] 
            and base.conhecimento[18,10] == respostas[0,10]):
            print(' Seu computador apresenta um problema de alimentação podendo ser causado pelo adaptador CA ou cabo de alimentação', 
                  'com defeito, bateria descarregada ou danificada, conexão incorreta ao notebook ou falha em um componente da placa',
                  'de sistema do notebook. Para resolver este problema realize os procedimentos:\n ',
                  '1 - verifique se o computador está recebendo energia do adaptador CA,Verifique se o adaptador CA não apresenta danos',
                  'e se está conectado corretamente a uma tomada de parede que esteja funcionando. Verifique se a alimentação de CA',
                  'está conectada à placa do sistema examinando se há danos no adaptador CA, na fiação e na conexão dos pinos. Os LEDs',
                  'do teclado se acendem quando a alimentação CA está conectada à placa do sistema. Componentes danificados, como o',
                  'adaptador CA ou o pino no conector de alimentação, exigem assistência técnica \n',
                  '2 - Use um adaptador de alimentação CA diferente Se tiver acesso a outro adaptador CA ou bateria fabricada para o', 
                  'computador, conecte ao computador e tente iniciá-lo. Caso tenha acesso a mais de um notebook, verifique se está',
                  'usando o adaptador que pertence ao computador.\n'
                  '3 - Remova a bateria e inicie o computador apenas com a alimentação CA Uma bateria descarregada ou defeituosa pode impedir', 
                  'que o adaptador CA forneça energia suficiente para iniciar o computador. Para verificar se a energia do adaptador',
                  'CA está disponível para o computador, remova a bateria, conecte o adaptador de alimentação CA e pressione o botão',
                  'Liga/Desliga. Se estiver disponível, tente usar outro adaptador CA que tenha sido aprovado para o computador e',
                  'repita esse teste.\n'
                  '4 - Remova o adaptador CA e inicie o computador apenas com a alimentação da bateria Um adaptador CA defeituoso não carrega',
                  'a bateria e impede que o computador inicie quando alimentado somente pela bateria. Para verificar se a energia de', 
                  'bateria está disponível para o computador, conecte o adaptador de alimentação CA, permita que a bateria carregue',
                  'por 30 minutos ou mais, desconecte o adaptador de alimentação e pressione o botão Liga/Desliga. Se uma bateria do',
                  'mesmo tipo de outro computador estiver disponível, tente usá-la totalmente carregada e repita esse teste.')

        elif(base.conhecimento[19,0] == respostas[0,0] and base.conhecimento[19,1] == respostas[0,1] 
            and base.conhecimento[19,2] == respostas[0,2] and base.conhecimento[19,3] == respostas[0,3]
            and base.conhecimento[19,4] == respostas[0,4] and base.conhecimento[19,5] == respostas[0,5] 
            and base.conhecimento[19,6] == respostas[0,6] and base.conhecimento[19,7] == respostas[0,7] 
            and base.conhecimento[19,8] == respostas[0,8] and base.conhecimento[19,9] == respostas[0,9] 
            and base.conhecimento[19,10] == respostas[0,10]):
            print('Quando um computador novo é usado pela primeira vez, o LED branco do conector de alimentação CA pisca',
                  'A bateria ainda está no "Modo de Transporte". A luz continua a pisca mesmo quando o adaptador CA é conectado.',
                  'Para resolver isso, desligue o notebook, conecte a alimentação CA, deixe a bateria carregar por pelo menos 30',
                  'minutos e inicie o computador.')
            
        elif(base.conhecimento[20,0] == respostas[0,0] and base.conhecimento[20,1] == respostas[0,1] 
            and base.conhecimento[20,2] == respostas[0,2] and base.conhecimento[20,3] == respostas[0,3]
            and base.conhecimento[20,4] == respostas[0,4] and base.conhecimento[20,5] == respostas[0,5] 
            and base.conhecimento[20,6] == respostas[0,6] and base.conhecimento[20,7] == respostas[0,7] 
            and base.conhecimento[20,8] == respostas[0,8] and base.conhecimento[20,9] == respostas[0,9] 
            and base.conhecimento[20,10] == respostas[0,10]):
            print('Nos modelos de computadores mais antigos, os diagnósticos de inicialização usam uma série de tons (bipes) para identificar',
                  'erros.\nCaso tenha substituído qualquer componente de hardware interno (módulos de memória, unidade de disco rígido etc.)',
                  'e observe uma código de luzes piscando ou de bipes, o componente pode não estar corretamente conectado. Para corrigir esse',
                  'problema, remova e recoloque os novos componentes.')
            
        elif(base.conhecimento[21,0] == respostas[0,0] and base.conhecimento[21,1] == respostas[0,1] 
            and base.conhecimento[21,2] == respostas[0,2] and base.conhecimento[21,3] == respostas[0,3]
            and base.conhecimento[21,4] == respostas[0,4] and base.conhecimento[21,5] == respostas[0,5] 
            and base.conhecimento[21,6] == respostas[0,6] and base.conhecimento[21,7] == respostas[0,7] 
            and base.conhecimento[21,8] == respostas[0,8] and base.conhecimento[21,9] == respostas[0,9] 
            and base.conhecimento[21,10] == respostas[0,10]):
            print('Uma tela preta sem nenhuma mensagem de erro geralmente indica um problema na funcionalidade básica de um componente crítico',
                  'Um componente de hardware, como um módulo de memória ou unidade de disco rígido ou disco de inicialização, foi instalado',
                  'incorretamente ou está solto porque o computador foi derrubado ou sofreu algum choque.')
            
        elif(base.conhecimento[22,0] == respostas[0,0] and base.conhecimento[22,1] == respostas[0,1] 
            and base.conhecimento[22,2] == respostas[0,2] and base.conhecimento[22,3] == respostas[0,3]
            and base.conhecimento[22,4] == respostas[0,4] and base.conhecimento[22,5] == respostas[0,5] 
            and base.conhecimento[22,6] == respostas[0,6] and base.conhecimento[22,7] == respostas[0,7] 
            and base.conhecimento[22,8] == respostas[0,8] and base.conhecimento[22,9] == respostas[0,9] 
            and base.conhecimento[22,10] == respostas[0,10]):
            print('Pode haver um problema com a instrução enviada do BIOS para um componente de hardware (por exemplo, falhas no',
                  'teclado) ou um driver de dispositivo incompatível.Geralmente pode ser resolvido com a instalação do firmware',
                  'atualizado de um componente crítico')
            
        elif(base.conhecimento[23,0] == respostas[0,0] and base.conhecimento[23,1] == respostas[0,1] 
            and base.conhecimento[23,2] == respostas[0,2] and base.conhecimento[23,3] == respostas[0,3]
            and base.conhecimento[23,4] == respostas[0,4] and base.conhecimento[23,5] == respostas[0,5] 
            and base.conhecimento[23,6] == respostas[0,6] and base.conhecimento[23,7] == respostas[0,7] 
            and base.conhecimento[23,8] == respostas[0,8] and base.conhecimento[23,9] == respostas[0,9] 
            and base.conhecimento[23,10] == respostas[0,10]):
            print('Há um conflito durante o carregamento de drivers e serviços.Geralmente pode ser resolvido',
                  'através da instalação de drivers atualizados ou da alteração da sequência de carregamento.',
                  'Uma mensagem de erro é exibida mas desaparece se o computador tentar reiniciar automaticamente.')
            
        elif(base.conhecimento[24,0] == respostas[0,0] and base.conhecimento[24,1] == respostas[0,1] 
            and base.conhecimento[24,2] == respostas[0,2] and base.conhecimento[24,3] == respostas[0,3]
            and base.conhecimento[24,4] == respostas[0,4] and base.conhecimento[24,5] == respostas[0,5] 
            and base.conhecimento[24,6] == respostas[0,6] and base.conhecimento[24,7] == respostas[0,7] 
            and base.conhecimento[24,8] == respostas[0,8] and base.conhecimento[24,9] == respostas[0,9] 
            and base.conhecimento[24,10] == respostas[0,10]):
            print('Há um conflito durante o carregamento de serviços e programas no ambiente Windows.',
                  'Em alguns casos, o computador pode tentar desligar e reiniciar, mas não conseguir reiniciar',
                  'totalmente no Windows.Pode ser necessário manter o botão Liga/Desliga pressionado por 15',
                  'segundos ou mais para forçar o computador a desligar.')
            
        elif(base.conhecimento[25,0] == respostas[0,0] and base.conhecimento[25,1] == respostas[0,1] 
            and base.conhecimento[25,2] == respostas[0,2] and base.conhecimento[25,3] == respostas[0,3]
            and base.conhecimento[25,4] == respostas[0,4] and base.conhecimento[25,5] == respostas[0,5] 
            and base.conhecimento[25,6] == respostas[0,6] and base.conhecimento[25,7] == respostas[0,7] 
            and base.conhecimento[25,8] == respostas[0,8] and base.conhecimento[25,9] == respostas[0,9] 
            and base.conhecimento[25,10] == respostas[0,10]):
            print('Se o computador tiver iniciado após a execução da redefinição física usando alimentação CA, desligue o computador,',
                  'insira a bateria e reinicie-o usando somente a bateria. Você também deve testar e calibrar a bateria, para',
                  'obter o melhor desempenho.aso tenha executado um ou mais dos processos para solução de problemas e o computador',
                  'iniciar normalmente no sistema operacional Windows, faça o seguinte para evitar problemas futuros:\n',
                  'Execute o Windows Update para atualizar o sistema operacional e o software\n',
                  'Execute um programa antivírus para remover qualquer vírus')
            
        elif(base.conhecimento[26,0] == respostas[0,0] and base.conhecimento[26,1] == respostas[0,1] 
            and base.conhecimento[26,2] == respostas[0,2] and base.conhecimento[26,3] == respostas[0,3]
            and base.conhecimento[26,4] == respostas[0,4] and base.conhecimento[26,5] == respostas[0,5] 
            and base.conhecimento[26,6] == respostas[0,6] and base.conhecimento[26,7] == respostas[0,7] 
            and base.conhecimento[26,8] == respostas[0,8] and base.conhecimento[26,9] == respostas[0,9] 
            and base.conhecimento[26,10] == respostas[0,10]):
            print('Se o computador de repente deixar de inicializar de forma apropriada, o primeiro procedimento',
                  'a ser realizado é executar a redefinição física. Efetuar a redefinição física poderá',
                  'corrigir muitos problemas. Se o computador ainda não iniciar corretamente realize os procedimentos:',
                  'Desconecte todos os dispositivos periféricos e remova todos os dispositivos USB e cartões de mídia SD\n',
                  'Desconecte o adaptador de alimentação CA, remova a bateria e mantenha pressionado o botão Liga/Desliga',
                  'por pelo menos 15 segundos para drenar toda a energia residual e restaurar as configurações',
                  'de inicialização padrão.')
            
        elif(base.conhecimento[27,0] == respostas[0,0] and base.conhecimento[27,1] == respostas[0,1] 
            and base.conhecimento[27,2] == respostas[0,2] and base.conhecimento[27,3] == respostas[0,3]
            and base.conhecimento[27,4] == respostas[0,4] and base.conhecimento[27,5] == respostas[0,5] 
            and base.conhecimento[27,6] == respostas[0,6] and base.conhecimento[27,7] == respostas[0,7] 
            and base.conhecimento[27,8] == respostas[0,8] and base.conhecimento[27,9] == respostas[0,9] 
            and base.conhecimento[27,10] == respostas[0,10]):
            print('Há um conflito durante o carregamento de drivers e serviços.Geralmente pode ser resolvido',
                  'através da instalação de drivers atualizados ou da alteração da sequência de carregamento.',
                  'Uma mensagem de erro é exibida mas desaparece se o computador tentar reiniciar automaticamente.')






