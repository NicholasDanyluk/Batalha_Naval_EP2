#********************************#  FUNÇÕES  #********************************#
import random
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


