PALAVRAS_PROIBÍDAS = {'futebol', 'religião', 'política'}
textos = ['João Gosta de futebol e política', 'A praia foi divertida']

for texto in textos:
    intersecao = PALAVRAS_PROIBÍDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado', texto)
