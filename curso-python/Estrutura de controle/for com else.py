PALAVRAS_PROIBÍDAS = ('futebol', 'religião', 'política')
# Se trocar alguma letra ou mudar a palavra de alguma forma, simplesmente vai autorizar os dois
textos = ['João Gosta de futebol e política', 'A praia foi divertida']

for texto in textos:

    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBÍDAS:
            print('Texto possui pelo menos uma palabra proibida:', palavra)
            break
    else:
        print('Texto autorizado', texto)
