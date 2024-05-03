#********************************#  FUNÇÕES  #********************************#
import random
from constantes import *
###############################################################################
###                     CRIA MATRIZ QUADRADA DE ESPAÇOS                     ###
###############################################################################

def cria_mapa(n):
    lista = []

    for i in range(n):
        l = [' ']*n
        lista.append(l)
    return lista

def cria_visual(n):
    lista = []

    for i in range(n):
        l = ['   ']*n
        lista.append(l)
    return lista

###############################################################################
###                    NAVIO PODE SER ALOCADO NA POSIÇÃO                    ###
###############################################################################

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
    
    for i in range(blocos):

        if orientacao == 'v':
            if linha+i >= len(mapa) or coluna >= len(mapa[linha+i]):
                return False
            elif mapa[linha+i][coluna] == 'N':
                return False
        
        elif orientacao == 'h':
            if linha >= len(mapa) or coluna+i >= len(mapa[linha]):
                return False
            elif mapa[linha][coluna+i] == 'N':
                return False

    return True

###############################################################################
###                    VERIFICA SE ACABOU OS Ns DA MATRIZ                   ###
###############################################################################

def foi_derrotado(mapa):

    for lista in mapa:

        for elemento in lista:

            if elemento == 'N':
                return False
    return True

###############################################################################
###                    ALOCANDO NAVIOS PARA O COMPUTADOR                    ###
###############################################################################

def aloca_navios(mapa,tamanhos):

    for t in tamanhos:
        pos = False
        while pos == False:
            n = len(mapa)
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            pos = posicao_suporta(mapa,t,linha,coluna,orientacao)
        for i in range (t):
            if orientacao == 'v':
                mapa[linha+i][coluna] = 'N'
            elif orientacao == 'h':
                mapa[linha][coluna+i] = 'N'
    return mapa

###############################################################################
###                      ALOCANDO NAVIOS PARA O JOGADOR                     ###
###############################################################################

def aloca_navios_jogador(mapa,tamanhos,mapa_visual):

    for t in tamanhos:
        pos = False
        while pos == False:
            n = len(mapa)
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            pos = posicao_suporta(mapa,t,linha,coluna,orientacao)
        for i in range (t):
            if orientacao == 'v':
                mapa[linha+i][coluna] = 'N'
                mapa_visual[linha+i][coluna] = f'{CORES['green']}{quadrado}{CORES['reset']}'
            elif orientacao == 'h':
                mapa[linha][coluna+i] = 'N'
                mapa_visual[linha][coluna+i] = f'{CORES['green']}{quadrado}{CORES['reset']}'
    return [mapa,mapa_visual]

###############################################################################
###                              PRINT DO MAPA                              ###
###############################################################################

def print_mapa(pais_pc,pais_jogador,visual_pc,visual_jogador):

    display = [f'''{CORES['reset'] + CORES['magenta'] + CORES['bold']}  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}{CORES['reset']}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
    for i in range(9):
        display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
    i+=1
    display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
    display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
    
    return display