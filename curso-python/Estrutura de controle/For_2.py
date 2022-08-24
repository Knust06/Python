from unicodedata import name


palavra = 'paralelepípedo'
for letra in palavra:
    # o end faz todas as letras ficarem na mesma linha, coisinha so pra deixar mais bonitinho do que cada letra em uma linha diferente
    print(letra, end=',')
    # voce pode colocar espaço, virgula
    print('Fim')

aprovados = ['Rafaela', 'Pedro,', 'Renato', 'Maria']
for name in aprovados:
    print(name)
for posicao, nome in enumerate(aprovados):
    print(f'{posicao})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
