import decimal
from decimal import Decimal, getcontext
print(dir(int))
print(dir(float))

a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)
print(type(a))

print(b.is_integer())
print(5.0.is_integer())
print((-3.6).__abs__())  # abs=função absoluta


# É uma especificação pois esses são números binários da esse numero 3.3000000000003
print(1.1 + 2.2)
Decimal(1) / Decimal(7)
getcontext().prec = 2  # Fazer com que o númerio de decimais tenha um limite.
print(Decimal(1.1)+Decimal(2.2))

dir(decimal)  # Para que possamos ver as funções dir por esse comando, é necessário importar o vocabulário para nao dar erro de sintaxe
