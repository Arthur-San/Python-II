import hashlib
import os

os.system("cls") #windows

# 1 - verificar os algoritomos disponíveis
print(hashlib.algorithms_available)

# 2 - os algoritimos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - utilizando o sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
menssage = 'teste testando o deste'.encode()

algorithm.update(menssage)

print(algorithm.hexdigest())

# 4 - utilizando o md5
menssage = 'teste testando o deste'.encode()
md5 = hashlib.md5()
md5.update(menssage)
print(md5.hexdigest())