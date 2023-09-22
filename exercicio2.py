## Agendamento de desligamento

# Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.

#LINK DE SITE DE COMANDOS
#https://www.uniaogeek.com.br/guia-de-comandos-cmd-terminal-do-windows/

import os

def agendarDesligamento(tempo):
    os.system(f"shutdown /s /t {tempo*60}")

def pararDesligamento():
    os.system('shutdown /a')

option = False

while option != True:
    print('o que deseja fazer?')
    print('1 - agendar delisgamento')
    print('2 - cancelar delisgamento')
    print('0 - sair')

    alter = int(input('->'))

    if alter == 1:
        tempo = int(input('Quanto tempo deseja agendar? (em minutos)'))
        agendarDesligamento(tempo)

    elif alter == 2:
        pararDesligamento()

    elif alter == 0:
        option = True
        print('Programa encerrado!')
    
    else:
        print('valor inválido')

