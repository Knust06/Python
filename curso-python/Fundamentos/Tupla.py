#tupla = tuple()
#tupla = ()
# type(tuple)
# dir(tupla)
# help(tuple)  # Sequencia IMUTÁVEL DE 'LISTA'
# tupla = ('um')  # string
# type(tupla)
#tupla = ('um',)
# print(type(tupla)) #tuple
tuple[0]
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])  # verde
print(cores[-1])  # branco
print(cores[1:])  # ('amarelo', 'azul', 'branco')
print(cores.index('amarelo'))  # amarelo está no índice 1
# Se não estiver escrito exatamente como você quer, ele não vai achar pois o azul está agr com o A maiusculo
print(cores.count('Azul'))
print(len(cores))  # possui 4 elementos dentro dessa tupla
print(type(cores))  # Classe tuple
