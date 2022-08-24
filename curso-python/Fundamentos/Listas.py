lista = []
print(type(lista))
print(dir(lista))
# lista é uma sequência MUTÁVEL ou seja pode ser modificada e é dinâmica.
lista.append(1)  # adicionar algo a lista
lista.append(5)
print(lista)
print(len(lista))
nova_lista = [1, 5, 'Ana', 'Bia']  # é uma estrutura que aceita uma heterogenia
print(nova_lista)  # [1, 5, 'Ana', 'Bia']
nova_lista.remove(5)
print(nova_lista)  # [1, 'Ana', 'Bia']
nova_lista.reverse()  # Reverte a ordem da lista e ALTERA DE FATO A LISTA.
print(nova_lista)  # 'Bia', 'Ana', 1]
# Cuidado ao usar listas heterogêneas num programa real para evitar erros e aumentar a previsibilidade


# Parte 2
lista1 = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista1.index('Guilherme')
# Posição 3. index busca saber a posição do elemento na lista
print(lista1.index('Guilherme'))
print(1 in lista1)  # True
print('Pedro 'not in lista1)
print(lista1[-1])  # Pega o último elemento da lista.
# Irá do final até o começo em busca do quinto elemento de trás para frente.
print(lista1[-5])


# Parte 3

lista2 = ['Ana', 'Lia', 'Rui', 'Pablo', 'Dani']
print(lista2[1:3])  # ['Lia', 'Rui']
print(lista2[1:-1])  # ['Lia', 'Rui', 'Pablo']
print(lista2[1:])  # ['Lia', 'Rui', 'Pablo', 'Dani']
print(lista2[:-1])  # ['Ana', 'Lia', 'Rui', 'Pablo']
print(lista2[:])  # ['Ana', 'Lia', 'Rui', 'Pablo', 'Dani']
print(lista2[::-1])  # Para contar desde o primeiro número
del lista2[2]  # deleta um elemento da lista
print(lista2)
del lista2[1:]  # Só sobra o elemento 0
