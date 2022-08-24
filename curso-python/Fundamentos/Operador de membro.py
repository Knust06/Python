# Operador de membro
lista = [1, 2, 3, 'Isabella', 'Lucas']
2 in lista  # True
'Isabella' not in lista  # False

# Operador de identidade
x = 3
y = x
z = 3
x is y  # True
y is z  # True
x is not z  # False # is not funciona not is não funciona devido a sintaxe
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b  # True
# False Embora tenha o mesmo conteúdo são listas diferentes como podemos ver no Pypreview
lista_b is lista_c
lista_a is not lista_c  # True são listas diferentes

# lista_c[1] = 200
# lista_a[1] = 200
