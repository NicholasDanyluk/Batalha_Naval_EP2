ori = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
ori_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m',
    'bold': '\u001b[1m',
    'underline': '\u001b[4m',
    'reversed': '\u001b[7m'
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

bemvindo = ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= '''

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

quadrado = '███'

barco = f'''{CORES['bold']}
                __/___            
          _____/______|           
  _______/_____\_______\______________
  \              < < <                |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n{CORES['reset']}'''


msg_vitoria = f'\n{CORES['reset']+CORES['bold']+CORES['underline']}PARABÉNS, VOCÊ É O NOVO REI DOS MARES!!! AQUI ESTA SEU TROFÉU!{CORES['reset']}\n'
msg_derrota = f'{CORES['reset']+CORES['bold']} VOCÊ NÃO AGUENTOU O PODER DOS MARES!!!{CORES['reset']}'

trofeu = f'''{CORES['yellow']}
        ##########################          
        ##########################          
   #####################################    
 #########################################  
####      ######################       #### 
###       ######################        ### 
##        ######################        ### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
 ####   ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ##################              
            ###{CORES['reset']+CORES['bold']}  REI DOS{CORES['reset']+CORES['yellow']}   ###              
            ###{CORES['reset']+CORES['bold']}   MARES{CORES['reset']+CORES['yellow']}    ###              
            ###            ###              
            ##################              
            ##################              
          ######################            
         ########################           {CORES['reset']}\n'''


gameover = f'''{CORES['reset']+CORES['bold']+CORES['red']}
     _____          __  __ ______    ______      ________ _____      
    / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \     
   | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |     
   | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /    
   | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \    
    \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\   
    {CORES['reset']}\n'''

tchau = f'''{CORES['bold']}

              |    |    |                         |    |    |              
             )_)  )_)  )_)                       )_)  )_)  )_)             
            )___))___))___)\                    )___))___))___)\           
           )____)____)_____)\\                 )____)____)_____)\\         
         _____|____|____|____\\\__           _____|____|____|____\\\__     
         \     ATÉ MAIS      /               \       MARUJO      /         
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^          
      {CORES['reset']}'''