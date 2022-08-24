print(2 + 3)
print('2' + '3')
# print (2 + '3') #TypeError: unsupported operand type(s) for +: 'int' and 'str' Da erro pois mistura inteiro com string

a = 2
b = '3'
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>

print(a + int(b))
print(str(a) + b)


# print(2 + int('2 daora')) o literal é invalido pois não tem como converter 2 daora para inteiro
