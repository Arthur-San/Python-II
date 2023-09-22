## Verificar conteúdo da String

# Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

import re
import os

os.system("cls") #windows


text = 'aoskdoaksdASDKOKASDOKA983984'

# verif = re.findall('[a-z]', text)
# print('Valores de [a-z]', verif)

# verif = re.findall('[A-Z]', text)
# print('Valores de [A-Z]', verif)

# verif = re.findall('[0-9]', text)
# print('Valores de [0-9]', verif)

def checarCarac(text):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(text)
    return not bool(string)

print(checarCarac(text))