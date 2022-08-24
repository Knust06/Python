# Tipo String
print(dir(str))
nome = 'Saulo Pedro'
nome
# nome[0] = 'P'       #String NÃO SUPORTA ALTERAÇÃO, ELA É IMUTÁVEL
print(nome[0])
# 'marca d'água'
# Dá erro de sintaxe pois fica uma string dentro de outra e não rola
# True pois simbolisam a mesma coisa.
print("Dias D'Avilla" == 'Dias D\'Avilla')
# Tem como usar apostrofo e aspas na mesma sentença
texto = 'Texto entre apostrófos pode ter "aspas"'
# Usa-se a contra-barra para mostrar ao python que as proximas aspas ou aapostrofo é parte do texto
"Teste \"funciona !"
print(texto)
doc = """ Texto com múltiplas
... linhas"""  # Usa-se 3 aspas para comentar ou fazer um texto com mais de uma linha.
print(doc)
doc = """ Texto com múltiplas
\t... linhas"""  # \t é a mesma função que apertar tab no word
print(doc)


# Parte 2


nome = 'Lucas Knust'
print(nome[0])  # L
print(nome[3])  # a
print(nome[-2])  # s
print(nome[4:])  # s Knust
print(nome[-5:])  # Knust
print(nome[:3])  # Luc não vai entrar o 3 pois é o indice final !
print(nome[2:5])  # cas
print(nome[::])  # Lucas Knust
print(nome[::2])  # LcsKut ele pula de dois em 2
print(nome[1::2])  # ua ns começa a partir do u em vez do L que é 0
print(nome[::-1])  # tsunK sacuL
print(nome[::-2])  # tuKscL pulando de dois em dois ao contrário


# Parte 3

frase = 'Python é muito louco'
'py' in frase  # False porque letras maiusculas e minusculas são diferentes.]
'ui' in frase  # True porque na palavra muito possui ui
print(len(frase))  # saber o tamanho da frase
print(frase.lower())  # tudo em minusculo mas NÃO MODIFICA A FRASE
print(frase.upper())  # tudo em maiusculo mas NÃO MODIFICA A FRASE.
# Para mudar de fato a frase é necessário:
frase = frase.upper()
print(frase)
# fazer esse comando quebra a frase ['PYTHON', 'É', 'MUITO', 'LOUCO']
print(frase.split())
print(frase.split('O'))  # Quebrou o O ['PYTH', 'N É MUIT', ' L', 'UC', '']
# dir(str)
# help(str.center)


# Parte 4

a = '123'
b = 'de Oliveira 4'
print(a + b)  # 123de Oliveira 4
# =
print(a.__add__(b))
# =
print(str.__add__(a, b))
print(len(a))  # 3
# =
print(a.__len__())

print('1' in a)  # True
# =
print(a.__contains__('1'))  # True
