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

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

#********************************#  FUNÇÕES  #********************************#

###############################################################################
###                     CRIA MATRIZ QUADRADA DE ESPAÇOS                     ###
###############################################################################

def cria_mapa(n):
    lista = []

    for i in range(n):
        l = [' ']*n
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

import random
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



#**********************************#  JOGO  #*********************************#

import random

### define o pais do computador ###
paises = ['Brasil','França','Austrália','Rússia','Japão']
p = ['1','2','3','4','5']
pais_pc = random.choice(paises)

### printa as mensagens iniciais ###
welcome = ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= '''

aviso = f'Iniciando o jogo!\n\nComputador está alocando os navios de guerra do país {pais_pc}...\nComputador já está em posição de batalha!'

config = '''
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes

2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado

3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro

4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino

5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino
'''

print(f'{welcome}\n\n{aviso}\n{config}')

### define o pais do jogador ###
jogador = input('Qual o número da nação da sua frota? ')
while jogador not in p:
    print('Opção inválida')
    jogador = input('Qual o número da nação da sua frota? ')
print(f'Você escolheu a nação {paises[int(jogador)-1]}\nAgora é sua vez de alocar seus navios de guerra!')
