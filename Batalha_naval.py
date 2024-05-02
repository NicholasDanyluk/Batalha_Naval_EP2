#******************************#  COMENTARIOS  #******************************#

# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m
# Reset: \u001b[0m
# bold: \u001b[1m
# underline: \u001b[4m
# reversed: \u001b[7m

#**********************************#  JOGO  #*********************************#

import random
import time
from funcoes import *
from constantes import *

### define o pais do computador ###
mapa = cria_mapa(10)
paises = ['Brasil','França','Austrália','Rússia','Japão']
p = ['1','2','3','4','5']
pais_pc = random.choice(paises)
navios_pc = []
for navio in PAISES[pais_pc]:
    for i in range(PAISES[pais_pc][navio]):
        navios_pc.append(CONFIGURACAO[navio])
mapa_pc = aloca_navios(mapa,navios_pc)


### printa as mensagens iniciais ###
welcome = CORES['magenta'] + CORES['bold'] + ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= ''' + CORES['reset']

aviso = CORES['magenta'] + CORES['bold'] + f'Iniciando o jogo!\n\n' + CORES['yellow'] + f'Computador está alocando os navios de guerra do país {CORES['underline'] + CORES['cyan']}{pais_pc}{CORES['reset'] + CORES['yellow']}...\nComputador já está em posição de batalha!' + CORES['reset']

config = f'''{CORES['magenta'] + CORES['bold']}
1: Brasil{CORES['reset'] + CORES['blue']}
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes
{CORES['magenta'] + CORES['bold']}
2: França{CORES['reset'] + CORES['blue']}
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado
{CORES['magenta'] + CORES['bold']}
3: Austrália{CORES['reset'] + CORES['blue']}
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro
{CORES['magenta'] + CORES['bold']}
4: Rússia{CORES['reset'] + CORES['blue']}
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino
{CORES['magenta'] + CORES['bold']}
5: Japão{CORES['reset'] + CORES['blue']}
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino
{CORES['reset']}'''

print(f'{welcome}\n\n{aviso}\n{config}')

### define o pais do jogador ###
jogador = input(CORES['yellow'] + f'Qual o número da nação da sua frota? {CORES['reset']}')
while jogador not in p:
    print(f'{CORES['red']}Opção inválida{CORES['reset']}\n')
    jogador = input(f'{CORES['yellow']}Qual o número da nação da sua frota? {CORES['reset']}')
print(f'{CORES['yellow']}Você escolheu a nação {CORES['cyan'] + CORES['underline']}{paises[int(jogador)-1]}{CORES['reset'] + CORES['yellow']}\nAgora é sua vez de alocar seus navios de guerra!\n')
pais_jogador = paises[int(jogador)-1]




### cria o mapa ###
visual_pc = cria_visual(10)
visual_jogador = cria_visual(10)
mapa_jogador = cria_mapa(10)

alocar = []
for navio in PAISES[pais_jogador]:
    for i in range(PAISES[pais_jogador][navio]):
        alocar.append(navio)

### loop de alocar navios ###

for i in range(len(alocar)):

    ### print do mapa ###
    display = [f'''{CORES['reset'] + CORES['magenta'] + CORES['bold']}  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}{CORES['reset']}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
    for i in range(9):
        display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
    i+=1
    display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
    display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
    for a in display:
        print(a)
    #####################

    blocos = CONFIGURACAO[alocar[0]]
    print(f'{CORES['reset'] + CORES['yellow']}Alocar: {CORES['cyan'] + CORES['underline']}{alocar[0]} ({blocos} blocos){CORES['reset']}')
    del alocar[0]
    if len(alocar) > 0:
        prox = alocar[0]
        for i in range(1,len(alocar)):
            prox += ', ' + alocar[i]
        print(f'{CORES['yellow']}Próximos: {prox}{CORES['reset']}')

    posicao = False

    while posicao == False:
        c = False

        while c == False:
            letra = input(f'{CORES['yellow']}Informe a letra: {CORES['reset']}')
            letra = letra.upper()
            if letra not in ori:
                print(f'{CORES['red']}Letra inválida{CORES['reset']}')
            else:
                c = True
        
        c = False
        while c == False:
            linha = input(f'{CORES['yellow']}Informe a linha: {CORES['reset']}')
            if linha not in ori_num:
                print(f'{CORES['red']}Linha inválida{CORES['reset']}')
            else:
                c = True

        c = False
        while c == False:
            orientacao = input(f'{CORES['yellow']}Informe a orientação [v/h]: {CORES['reset']}')
            orientacao.lower()
            if orientacao != 'v' and orientacao != 'h':
                print(f'{CORES['red']}Orientação inválida{CORES['reset']}')
            else:
                c = True

        l = int(linha)-1
        c = ori[letra]
        posicao = posicao_suporta(mapa_jogador,blocos,l,c,orientacao)
        if posicao == False:
            print(f'{CORES['red']}Não foi possivel alocar o navio em {CORES['cyan'] + CORES['underline']}{letra}{linha} {orientacao}{CORES['reset']}\n')
            ### print do mapa ###
            display = [f'''{CORES['magenta'] + CORES['bold']}  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}{CORES['reset']}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
            for i in range(9):
                display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
            i+=1
            display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
            display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
            for a in display:
                print(a)
            #####################
            print(f'{CORES['reset'] + CORES['yellow']}Alocar: {CORES['cyan']+CORES['underline']}{alocar[0]} ({blocos} blocos){CORES['reset']}')
            if len(alocar) > 0:
                prox = alocar[0]
                for i in range(1,len(alocar)):
                    prox += ', ' + alocar[i]
                print(f'{CORES['yellow']}Próximos: {prox}{CORES['reset']}')

    print(f'{CORES['green']}Navio alocado!{CORES['reset']}\n')

    for i in range(blocos):
        if orientacao == 'v':
            mapa_jogador[l+i][c] = 'N'
            visual_jogador[l+i][c] = f'{CORES['green']}{quadrado}{CORES['reset']}'
        elif orientacao == 'h':
            mapa_jogador[l][c+i] = 'N'
            visual_jogador[l][c+i] = f'{CORES['green']}{quadrado}{CORES['reset']}'

### start print ###
print(f'\n{CORES['reset'] + CORES['cyan'] + CORES['bold'] + CORES['underline']}Iniciando batalha naval!{CORES['reset']}\n')
tempos = [5,4,3,2,1]
for tempo in tempos:
    print(tempo)
    time.sleep(1)

print(barco)
vitoria_pc = False
vitoria_jogador = False

### loop do jogo ###
restart = 's'
while restart == 's':
    while vitoria_jogador == False and vitoria_pc == False:
        ### print do mapa ###
        display = [f'''\n{CORES['reset'] + CORES['magenta'] + CORES['bold']}  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}{CORES['reset']}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
        for i in range(9):
            display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
        i+=1
        display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
        display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
        for a in display:
            print(a)
        #####################
        print(f'{CORES['yellow']}Cordenadas do seu disparo{CORES['reset']}')

        ### bomba do jogador ###
        posi = False
        while posi == False:
            c = False
            while c == False:
                letra = input(f'{CORES['yellow']}Informe a letra: {CORES['reset']}')
                letra = letra.upper()
                if letra not in ori:
                    print(f'{CORES['red']}Letra inválida{CORES['reset']}')
                else:
                    c = True
            
            c = False
            while c == False:
                linha = input(f'{CORES['yellow']}Informe a linha: {CORES['reset']}')
                if linha not in ori_num:
                    print(f'{CORES['red']}Linha inválida{CORES['reset']}')
                else:
                    c = True

            l = int(linha)-1
            c = ori[letra]
            if mapa_pc[l][c] != 'B' and mapa_pc[l][c] != 'A':
                posi = True
            else:
                print(f'{CORES['red']}Posição {CORES['cyan'] + CORES['bold'] + CORES['underline']}{letra}{linha}{CORES['reset'] + CORES['red']} já Bombardeada!{CORES['reset']}')
        if mapa_pc[l][c] == 'N':
            mapa_pc[l][c] = 'B'
            visual_pc[l][c] = f'{CORES['red']}{quadrado}{CORES['reset']}'
        else:
            mapa_pc[l][c] = 'A'
            visual_pc[l][c] = f'{CORES['blue']}{quadrado}{CORES['reset']}'
        letra1 = letra
        linha1 = linha

        ### bomba do computador ###
        pos = False
        while pos == False:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if mapa_jogador[linha][coluna] == ' ' or mapa_jogador[linha][coluna] == 'N':
                pos = True
                if mapa_jogador[linha][coluna] == 'N':
                    mapa_jogador[linha][coluna] = 'B'
                    visual_jogador[linha][coluna] = f'{CORES['red']}{quadrado}{CORES['reset']}'
                elif mapa_jogador[linha][coluna] == ' ':
                    mapa_jogador[linha][coluna] = 'A'
                    visual_jogador[linha][coluna] = f'{CORES['blue']}{quadrado}{CORES['reset']}'
            


        ori1 = {}
        for key,valor in ori.items():
            ori1[valor+1] = key

        ### prints ###
        if mapa_jogador[linha][coluna] == 'A':
            jog = f'{CORES['blue'] + CORES['bold']}Água!{CORES['reset']}'
        elif mapa_jogador[linha][coluna] == 'B':
            jog = f'{CORES['red'] + CORES['bold']}BOOOOMMMMM!{CORES['reset']}'
        
        if mapa_pc[l][c] == 'A':
            pc = f'{CORES['blue'] + CORES['bold']}Água!{CORES['reset']}'
        elif mapa_pc[l][c] == 'B':
            pc = f'{CORES['red'] + CORES['bold']}BOOOOMMMMM!{CORES['reset']}'


        print(f'{CORES['reset']}Jogador ---->>>> {CORES['cyan'] + CORES['bold'] + CORES['underline']}{letra1}{linha1}{CORES['reset']}    {pc}\nComputador ---->>>> {CORES['cyan'] + CORES['bold'] + CORES['underline']}{ori1[coluna+1]}{linha+1}{CORES['reset']}    {jog}')

        vitoria_jogador = foi_derrotado(mapa_pc)
        vitoria_pc = foi_derrotado(mapa_jogador)

        if vitoria_jogador == True:
            print(f'{CORES['magenta'] + CORES['bold']}Você venceu!\nTemos um novo xerife nos mares!{CORES['reset']}')
        elif vitoria_pc == True:
            print(f'{CORES['magenta'] + CORES['bold']}Você perdeu!\nO computador ainda é o senhor dos mares{CORES['reset']}')

    restart = (input(f'{CORES['yellow']}Jogar novamente? [s/n] {CORES['reset']}')).lower()
    vitoria_pc = False
    vitoria_jogador = False
print('\n\nAté a proxima!')