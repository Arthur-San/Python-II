import random
import os #linux

os.system('clear')


# 1 - selecionao o valor aleatório de uma lista
list = [7, 6, 5, 2, 7, 8, 1, 0]

print(random.choice(list))

# 2 - gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - seleciona mais de um valor aleatório
# sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list, 2))
print(random.sample(list, 3))
s = "testando o teste"
print(random.sample(s, 2))