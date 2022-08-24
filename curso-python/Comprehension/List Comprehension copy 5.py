dicionario = {i: i *2 for i in range(10) if i % 2 == 0}
# dicionario = {f'Item{i}': i *2 for i in range(10) if i % 2 == 0} para colocar item0 = 0 item 2 = 4 item 4 =8
#print(dicionario)
for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
