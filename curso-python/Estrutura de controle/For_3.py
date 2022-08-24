produto = {'nome': 'Caneca Bonita', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto:
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
