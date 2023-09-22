import math

#MÓDULOS - BUILT IN (NATIVOS DO PYTHON)

# 1 - acessar o número PI
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - acessar o numero de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - arredondando numeros para cima e baixo
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

# 4 - fatorial de um numero
num2 = 5 # !5 = 120
print(math.factorial(num2))

# 5 - potência de numeros
num3 = 5
print(math.pow(5,2))

# 6 - raiz quadrada de um numero
print(math.sqrt(169))

# 7 - MDC
mdc= math.gcd(25,100)
print(mdc)

# 8 - logaritimo
print(math.log(10))