# Conjunto não aceita repetição, não é indexado e não garante ordem de inserção
a = {1, 2, 3}
print(type(a))  # <class 'set'>

a = set('codddddd3r')  # Sem repetição
print(a)  # {'o', 'c', '3', 'r', 'd'}
print(3 in a, 4 not in a)  # não possui 3 numérico e sim 3 string #False e True
print('3' in a, 4 not in a)  # True e True
# True pois tem os mesmos elementos e os repetidos são ignorados
print({1, 2, 3} == {3, 2, 1, 3})


# Operação
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))  # {1, 2, 3}
print(c1.intersection(c2))  # {2}
c1.update(c2)
print(c1)  # {1, 2, 3}
# True pq eu fiz o update no c1 com elementos do c2. Na linha 18. Sem ele essa afirmação daria falsa
print(c2 <= c1)
print(c1 >= c2)  # True (mesma coisa do de cima :P)
print({1, 2, 3} - {2, 3})  # {1}
print(c1 - c2)  # {1}
c1 -= {2}
print(c1)  # {1, 3}
