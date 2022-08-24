from string import Template

nome, idade = 'Ana', 30.9875
# Nome: Ana Idade: 30 #% depois do %d é para separar a string do valor que vc quer colocar
print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: %s Idade: %f' % (nome, idade))  # %f vira float ponto flutuante.
# %2.f duas casas decimais apenas 30.99
print('Nome: %s Idade: %.2f' % (nome, idade))
# Nome: Ana Idade: 30 True False
print('Nome: %s Idade: %d %r %r' % (nome, idade, True, False))
print('Nome: %s Idade: %d %d %d' %
      (nome, idade, True, False))  # Nome: Ana Idade: 30 1 0
print('Nome: {0} Idade: {1}'.format(nome, idade))  # python < 3.6
print(f'Nome: {nome} Idade: {idade} {2 ** 8 + 1}')
# Formas básicas para fazer a interpolação

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))  # Nome: Ana Idade: 30.9875
print(s.substitute(nome=nome, idade=idade))  # Nome: Ana Idade: 30.9875
