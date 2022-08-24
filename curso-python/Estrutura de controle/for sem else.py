PALAVRAS_PROIBÍDAS = ('futebol', 'religião', 'política')
textos = ['João Gosta de futebol e política', 'A praia foi divertida']

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBÍDAS:
            print('Texto possui pelo menos uma palabra proibida:', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado', texto)
