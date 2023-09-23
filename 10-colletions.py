from collections import Counter, namedtuple, deque
from operator import itemgetter
import os

os.system('clear')

# 1 - contar itens de uma lista
fruits = ["maça", "banana", "uva", "pera", "uva", "pera", "maça", "laranja", "uva", "banana"]

print(fruits)
print(Counter(fruits))

# 2 - utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('fifa12', 90.50, 8)
g2 = game('RE 4', 20.99, 9.7)
print(g1)
print(g2)

# 3 - ordenando dicionários
studants = {'Pedro':23, "Ana":22, "Ronaldo":26, "Janaina":25 }
a = sorted(studants.items(), key=itemgetter(0)) #key=itemgetter(0) irá ordenar de acordo com o indice 0
print(studants)
print(a)

# 4 - utilizando fila ambas extremidades
deq = deque([20, 40, 60,80])
deq.appendleft(10)
print(deq)

deq.append(90)
print(deq)

deq.popleft()
print(deq)

deq.pop()
print(deq)
