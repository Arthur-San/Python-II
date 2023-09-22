import re
import os

os.system('clear') # limpar terminal antes

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'
# 1 - indice inicial e final de palavras
# O "r" siginifica que estamos trabalhando com uma string bruta (raw string)

match = re.search(r'sem limites', text)
print('Indice inicial', match.start())
print('Indice final', match.end())

# 2 - buscando o índice que possui o ponto
site = 'https:/www.onebitcode.com'
#match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

# 3 - buscando uma lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4 - verificando o início de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não Corresponde: {f}")

# 5 - verificando o final de uma string
rule_end = r'!$'
phrases2 = 'O dia está lindo!'
match = re.search(rule_end, phrases2)

if match:
    print('Sim, corresponde')
else:
    print('Não corresponde')