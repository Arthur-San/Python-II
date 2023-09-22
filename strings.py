## Módulo de strings

# Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

# 1. Inverter uma string de trás pra frente.
# 2. Retornar apenas letras com índice par.
# 3. Retornar apenas letras com índice ímpar.

def intertString(texto):
    print(texto[::-1])

def buscarLetraIndicePar(texto):
    print('Letras de índice par: ', texto[::2])
        
def buscarLetraIndiceImpar(texto):
    print('Letras de índice ímpar: ', texto[1::2])
    


    

