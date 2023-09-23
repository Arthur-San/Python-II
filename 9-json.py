import json

# 1 - strings para dicionarios
person = '{"name":"Arthur","languagens": ["Python", "Java"]}'
person_dict = json.loads(person)

print(person_dict)

# 2 - convertendo dicionario para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Criando json em txt
with open("person.log", "w") as json_file: # w - cria 
    json.dump(person_dict, json_file)

# 4.1 - adicionando em json em txt
with open("person.log", "a") as json_file: # a - append
    json.dump(person_dict, json_file)

# 5 lendo json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)