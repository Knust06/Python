True or False
print(7 != 3 and 2 > 3)  # 7 != 3 true e 2 > 3 false
# Se estiver ensolarado e tiver dinheiro vou na praia(True)
# Se estiver ensolarado e não tiver dinheiro eu nao vou na praia(False)
# As duas condições precisam ser verdadeiras para ser verdadeiro

# Tabela verdade do AND
True and True  # True
True and False  # False
False and False  # False
False and True  # False
# Python é parecido com inglês
# Verdadeiro pois tudo é verdadeiro
print(True and True and True and True and True and True and True)
# Basta uma falsa e tudo se torna falso
print(True and True and False and True and True and True and True)

# Tabela verdade do OR
True or True  # True
True or False  # True
False or True  # True
False or False  # False
# Será verdadeiro pois existe pelo menos uma Verdadeira
print(False or False or False or False or True)

# Tabela verdade do XOR
True != True  # False
True != False  # True
False != True  # True
False != False  # False
# Para que seja Verdadeiro é necessário que seja  exclusivamente um ou o outro

# Operador de Negação (Unário)
not True  # False
not False  # True
# Basicamente o contrário
print(not 0)  # True
print(not 12718921789)  # False
# Pois o 0 é falso e qualquer outro número é verdadeiro
print(not -1)  # False
print(not not -1)  # verdadeiro(Volta ao valor original)
print(not not True)  # True

# Cuidado! Operador Bit-a-Bit
True & True  # True
True & False  # False
False | True  # True # Operador ou, Pipe
True ^ False  # True

# AND Bit-a-Bit
# 3 = 11  # Valor para binário
# 2 = 10
# Resultado(_) = 10 = 2
print(3 & 2)  # = 2
# Resultado Bit a Bit

# OR Bit-a-Bit
# 3 = 11  # Valor para binário
# 2 = 10
# Resultado(_) = 11 = 3
print(3 | 2)  # = 3

# XOR Bit-a-Bit

# 3 = 11  # Valor para binário
# 2 = 10
# Resultado(_) = 01 = 1
print(3 ^ 2)  # = 1

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas > - 0.2 * salario
print(meta)  # True

saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas > - 0.2 * salario
meta = saldo_positivo ^ despesas_controladas
print(meta)
