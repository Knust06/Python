pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': [
    'Inglês', 'Português']}
print(type(pessoa))  # dict ou dicionário <class 'dict'>
print(dir(dict))
print(len(pessoa))  # Possui 3 informações nesse dicionário

pessoa = {123: 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
# Modifiquei o nome pelo 123 e ainda funciona com valores inteiros sem problemas.
print(pessoa)

# Isso só da certo pois idade NÃO É MAIS UMA STRING e sim uma variável.
idade = 'Bla Bla'
pessoa = {'nome': 'Prof(a). Ana', idade: 38, 'cursos': ['Inglês', 'Português']}
print(pessoa)
print(pessoa['nome'])
print(idade)  # não está funcionando aqui pois eu coloquei outro valor para idade no exemplo acima mas é tranquilo de entender
print(pessoa['cursos'])  # Inglês e Portguês
print(pessoa['cursos'][1])  # Português
# print(pessoa['tags']) #Não consegue executar pois tags não existe dentro do dict pessoa
print(pessoa.keys())  # dict_keys(['nome', 'Bla Bla', 'cursos'])
# dict_values(['Prof(a). Ana', 38, ['Inglês', 'Português']])
print(pessoa.values())
# dict_items([('nome', 'Prof(a). Ana'), ('Bla Bla', 38), ('cursos', ['Inglês', 'Português'])])
print(pessoa.items())
print(pessoa.get(idade))  # 38
print(pessoa.get('tags'))  # Vira um array vazio.
# Array é um tipo de sequência que funciona bem parecido com lista, armazenando algo restringido


# Dicionário parte 2

pessoa = {'nome': 'Prof.Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
# Coloca algo dentro de um objeto no dicionário no caso foi curso angular dentro de curso
pessoa['cursos'].append('Angular')
# {'nome': 'Prof.Alberto', 'idade:': 43, 'cursos': ['React', 'Python', 'Angular'], 'idade': 44}
print(pessoa)
pessoa.pop('idade')
# {'nome': 'Prof.Alberto', 'cursos': ['React', 'Python', 'Angular']}
print(pessoa)
# O pop le o valor e remove
pessoa.update({'idade': 40, 'Sexo': 'M'})
# Update atualiza informações no nosso dicionário tirando, modificando e colocando informações
del pessoa['cursos']  # deleta toda uma parte do dicionário específica.
pessoa.clear()  # Tornou um dicionário completamente limpo ele limpa todo o dicionário
